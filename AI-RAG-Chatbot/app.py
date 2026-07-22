import os
import time
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import create_embedding_model, split_documents

load_dotenv()

DB_PATH = "vectorstore"

EXAMPLE_QUESTIONS = [
    "What is this document about?",
    "Summarize the key points in 3 bullet points.",
    "Explain the main concept like I'm a beginner.",
]

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI PDF RAG Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass


load_css()

# -----------------------------
# LOAD VECTOR DATABASE
# -----------------------------

@st.cache_resource
def load_embedding_model():
    return create_embedding_model()


def load_vector_database(_embedding_model):
    if not os.path.exists(DB_PATH):
        return None
    return FAISS.load_local(
        DB_PATH,
        _embedding_model,
        allow_dangerous_deserialization=True
    )


def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0.2,
    )


embedding_model = load_embedding_model()

# vector_db lives in session_state (not cache_resource) so that adding new
# PDFs at runtime is reflected immediately without needing a restart
if "vector_db" not in st.session_state:
    st.session_state.vector_db = load_vector_database(embedding_model)

llm = load_llm()

# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_docs" not in st.session_state:
    st.session_state.last_docs = []

# -----------------------------
# CORE RAG LOGIC
# -----------------------------

def build_prompt(question, context, history_text):
    return f"""You are a helpful AI assistant answering questions about the user's uploaded PDF documents.

Rules:
- Answer ONLY using the given context below.
- If the answer is not available in the context, reply exactly:
  "I couldn't find the answer in the uploaded documents."
- Use the recent conversation for follow-up questions (e.g. "explain more", "what about X") but never invent facts outside the context.
- Be concise and use bullet points when helpful.

Recent conversation:
{history_text}

Context from documents:
{context}

Question:
{question}

Answer:
"""


def get_recent_history_text(max_turns=3):
    recent = st.session_state.messages[-(max_turns * 2):]
    lines = []
    for m in recent:
        role = "User" if m["role"] == "user" else "Assistant"
        lines.append(f"{role}: {m['content']}")
    return "\n".join(lines) if lines else "(no previous conversation)"


def stream_answer(question):
    vector_db = st.session_state.vector_db

    if vector_db is None:
        yield "⚠️ No documents indexed yet. Upload a PDF from the sidebar first."
        st.session_state.last_docs = []
        return

    docs = vector_db.similarity_search(question, k=4)
    st.session_state.last_docs = docs

    context = "\n\n".join(doc.page_content for doc in docs)
    history_text = get_recent_history_text()
    prompt = build_prompt(question, context, history_text)

    for chunk in llm.stream(prompt):
        text = chunk.content
        if isinstance(text, list):
            text = "".join(
                item.get("text", "") for item in text if isinstance(item, dict)
            )
        if text:
            yield text


def add_pdf_to_index(uploaded_file):
    """Save an uploaded PDF, chunk it, and add it to the FAISS index."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name

    try:
        loader = PyPDFLoader(tmp_path)
        raw_docs = loader.load()

        for doc in raw_docs:
            doc.metadata["source"] = uploaded_file.name

        chunks = split_documents(raw_docs)

        if st.session_state.vector_db is None:
            st.session_state.vector_db = FAISS.from_documents(chunks, embedding_model)
        else:
            st.session_state.vector_db.add_documents(chunks)

        st.session_state.vector_db.save_local(DB_PATH)
        return len(chunks)
    finally:
        os.remove(tmp_path)


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:
    st.title("📚 RAG Chatbot")
    st.success("PDF Q&A powered by Gemini")

    st.markdown("---")
    st.subheader("📤 Add a document")

    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"], label_visibility="collapsed")

    if uploaded_file is not None:
        if st.button("➕ Add to knowledge base", use_container_width=True):
            with st.spinner(f"Indexing {uploaded_file.name}..."):
                n_chunks = add_pdf_to_index(uploaded_file)
            st.success(f"Added {n_chunks} chunks from {uploaded_file.name}")
            st.rerun()

    st.markdown("---")
    st.subheader("⚙ Technology")
    st.info("Embedding\n\nall-MiniLM-L6-v2")
    st.info("LLM\n\nGemini Flash")
    st.info("Vector Database\n\nFAISS")

    st.markdown("---")

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🗑 Clear chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.last_docs = []
            st.rerun()
    with col_b:
        chat_text = "\n\n".join(
            f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages
        )
        st.download_button(
            "💾 Export",
            data=chat_text if chat_text else "No messages yet.",
            file_name="chat_history.txt",
            use_container_width=True,
        )

# -----------------------------
# TITLE + METRICS
# -----------------------------

st.markdown(
    """
# 🤖 AI PDF RAG Chatbot

Ask questions about your PDF documents using **LangChain + FAISS + Gemini**.
"""
)

n_vectors = 0
if st.session_state.vector_db is not None:
    try:
        n_vectors = st.session_state.vector_db.index.ntotal
    except Exception:
        n_vectors = 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🧩 Chunks indexed", n_vectors)
with col2:
    st.metric("🧠 Embedding", "MiniLM")
with col3:
    st.metric("🤖 LLM", "Gemini Flash")

st.markdown("---")

# -----------------------------
# EXAMPLE QUESTIONS (clickable)
# -----------------------------

if not st.session_state.messages:
    st.markdown("**Try asking:**")
    cols = st.columns(len(EXAMPLE_QUESTIONS))
    for col, q in zip(cols, EXAMPLE_QUESTIONS):
        with col:
            if st.button(q, use_container_width=True):
                st.session_state.pending_question = q
                st.rerun()

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------

for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------

question = st.chat_input("💬 Ask a question about your PDFs...")

if "pending_question" in st.session_state:
    question = st.session_state.pop("pending_question")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(question)

    with st.chat_message("assistant", avatar="🤖"):
        answer = st.write_stream(stream_answer(question))

        docs = st.session_state.last_docs
        if docs:
            with st.expander("📄 View retrieved sources"):
                for i, doc in enumerate(docs):
                    source = doc.metadata.get("source", "Unknown")
                    page = doc.metadata.get("page", 0) + 1
                    st.markdown(f"**Result {i + 1} — {source} (page {page})**")
                    st.code(doc.page_content[:600])

    st.session_state.messages.append({"role": "assistant", "content": answer})

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📚 LangChain")
with col2:
    st.info("🗄️ FAISS")
with col3:
    st.info("🤖 Gemini")

st.markdown(
    """
<div style="text-align:center; padding:15px; color:gray;">
Built using <b>Streamlit</b> | <b>LangChain</b> | <b>FAISS</b> |
<b>Sentence Transformers</b> | <b>Google Gemini</b>
</div>
""",
    unsafe_allow_html=True,
)