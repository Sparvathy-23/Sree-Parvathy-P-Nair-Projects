#  AI PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from PDF documents using semantic search and Google's Gemini Large Language Model.

This project demonstrates the complete RAG pipeline including document loading, preprocessing, chunking, embedding generation, vector database creation, similarity search, LLM integration, and a Streamlit-based chatbot interface.

---

# Features

- Load PDF documents
- Split documents into semantic chunks
- Generate sentence embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Perform semantic similarity search
- Generate answers using Google Gemini
- Maintain conversation history
- Upload new PDF documents through the Streamlit interface
- Display retrieved document sources
- Export chat history
- Interactive web interface built with Streamlit

---

# Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Google Gemini API
- PyPDF
- Hugging Face Transformers
- python-dotenv

---

# Project Structure

```
CHATBOT/
│
├── data/
│   ├── Python_Basics.pdf
│   ├── Machine_Learning_Fundamentals.pdf
│   └── Deep_Learning_Introduction.pdf
│
├── results/
│   ├── dashboard.png
│   ├── dashboard1.png
│   ├── dashboard2.png
│   └── demo.mp4
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── app.py
├── loader.py
├── chunking.py
├── embeddings.py
├── vector_store.py
├── similarity_search.py
├── rag.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Project Workflow

```
PDF Documents
      │
      ▼
Load PDFs
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store Embeddings in FAISS
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Gemini LLM
      │
      ▼
Generate Final Answer
      │
      ▼
Display Response in Streamlit
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/yourrepository.git

cd CHATBOT
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Gemini API

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

**Do not upload the `.env` file to GitHub.**

---

# Build the Vector Database

Run once after adding PDF documents.

```bash
python vector_store.py
```

---

# Run the Streamlit Application

```bash
streamlit run app.py
```

---

# Sample Questions

- What is supervised learning?
- Explain CNN.
- What are transformers?
- What are Python data types?
- What is overfitting?
- Summarize the uploaded document.
- Explain the topic like I am a beginner.

---

# Screenshots

## Dashboard

Add screenshots from the `results` folder.

```
results/dashboard.png
results/dashboard1.png
results/dashboard2.png
```

---

# Demo Video

```
results/demo.mp4
```

---

# Files Description

| File | Description |
|------|-------------|
| app.py | Streamlit web application |
| loader.py | Loads PDF documents |
| chunking.py | Splits documents into chunks |
| embeddings.py | Generates sentence embeddings |
| vector_store.py | Creates and saves the FAISS vector database |
| similarity_search.py | Retrieves relevant chunks using semantic search |
| rag.py | Connects the retriever with the Gemini LLM |
| utils.py | Helper functions used across the project |

---

# RAG Pipeline

1. Load PDF documents.
2. Extract text from PDFs.
3. Split text into overlapping chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks based on the user's query.
7. Pass the retrieved context to the Gemini LLM.
8. Generate a context-aware response.
9. Display the response and retrieved sources in Streamlit.

---

# Future Improvements

- Support DOCX and TXT files
- Multiple embedding models
- Persistent conversation memory
- OCR support for scanned PDFs
- Cloud deployment
- Multi-user authentication

---

# Author

**Sree Parvathy**

B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Capstone Project