from langchain_community.vectorstores import FAISS
from utils import create_embedding_model

DB_PATH = "vectorstore"


def load_vector_database():
    """
    Load the saved FAISS vector database.
    """
    embedding_model = create_embedding_model()

    vector_db = FAISS.load_local(
        DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_db


def search_documents(vector_db, query, k=3):
    """
    Search the vector database.
    """
    results = vector_db.similarity_search(query, k=k)
    return results


def main():

    vector_db = load_vector_database()

    while True:

        print("\n" + "=" * 80)

        query = input("Enter your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = search_documents(vector_db, query)

        print("\nTop Matching Chunks\n")

        for i, doc in enumerate(results):

            print("=" * 80)
            print(f"Result {i+1}")
            print("-" * 80)

            print("Source :", doc.metadata["source"])
            print("Page   :", doc.metadata["page"] + 1)

            print("\nContent:\n")

            print(doc.page_content)

            print()


if __name__ == "__main__":
    main()