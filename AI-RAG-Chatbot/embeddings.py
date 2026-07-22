from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "data"


def load_documents():
    """
    Load all PDF documents from the data folder.
    """
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()
    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = splitter.split_documents(documents)

    return chunks


def create_embedding_model():
    """
    Load the sentence embedding model.
    """
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


def main():

    documents = load_documents()

    chunks = split_documents(documents)

    embedding_model = create_embedding_model()

    print("=" * 80)
    print("Embedding Model Loaded Successfully")
    print("=" * 80)

    print(f"\nTotal Chunks : {len(chunks)}")

    print("\nGenerating embedding for first chunk...\n")

    embedding = embedding_model.embed_query(
        chunks[0].page_content
    )

    print("Embedding Dimension :", len(embedding))

    print("\nFirst 20 Values:\n")

    print(embedding[:20])


if __name__ == "__main__":
    main()