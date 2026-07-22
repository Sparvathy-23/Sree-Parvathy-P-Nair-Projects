from langchain_community.vectorstores import FAISS
from utils import (
    load_documents,
    split_documents,
    create_embedding_model,
)

DB_PATH = "vectorstore"


def create_vector_database(chunks, embedding_model):
    """
    Create and save the FAISS vector database.
    """
    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vector_db.save_local(DB_PATH)

    return vector_db


def main():

    print("Loading documents...")

    documents = load_documents()

    print(f"Documents Loaded : {len(documents)}")

    chunks = split_documents(documents)

    print(f"Chunks Created : {len(chunks)}")

    embedding_model = create_embedding_model()

    print("Embedding Model Loaded")

    create_vector_database(
        chunks,
        embedding_model
    )

    print("\nVector Database Saved Successfully!")


if __name__ == "__main__":
    main()