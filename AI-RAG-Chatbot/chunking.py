from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
DATA_PATH = "data"


def load_documents():
    """
    Load all PDF documents.
    """
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()
    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


def main():

    documents = load_documents()

    print(f"\nTotal Pages : {len(documents)}")

    chunks = split_documents(documents)

    print(f"Total Chunks : {len(chunks)}")

    print("\n")

    for i, chunk in enumerate(chunks):

        print("=" * 80)

        print(f"Chunk {i+1}")

        print("-" * 80)

        print(chunk.page_content)

        print("\n")


if __name__ == "__main__":
    main()