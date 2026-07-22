import os

from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import create_embedding_model

# Load environment variables
load_dotenv()

DB_PATH = "vectorstore"


def load_vector_database():

    embedding_model = create_embedding_model()

    vector_db = FAISS.load_local(
        DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_db


def create_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0
    )

    return llm


def retrieve_context(vector_db, query):

    docs = vector_db.similarity_search(query, k=3)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return context


def ask_question(vector_db, llm, question):

    context = retrieve_context(vector_db, question)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

If the answer is not found in the context, reply:

"I couldn't find the answer in the provided documents."

Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)
    if isinstance(response.content, str):
        return response.content

    if isinstance(response.content, list):
        answer = ""

        for item in response.content:
            if isinstance(item, dict) and item.get("type") == "text":
                answer += item.get("text", "")

        return answer.strip()
    return str(response.content)


def main():

    print("Loading Vector Database...")

    vector_db = load_vector_database()

    print("Loading Gemini...")

    llm = create_llm()

    print("RAG Chatbot Ready!")

    while True:

        print("\n" + "=" * 80)

        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_question(
            vector_db,
            llm,
            question
        )

        print("\nAnswer\n")

        print(answer)


if __name__ == "__main__":
    main()