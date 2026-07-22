from langchain_community.document_loaders import PyPDFDirectoryLoader

# Folder containing the PDF files
DATA_PATH = "data"

def load_documents():
    """
    Load all PDF files from the data folder.
    """
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()
    return documents


def main():
    documents = load_documents()

    print("=" * 80)
    print(f"Total Pages Loaded: {len(documents)}")
    print("=" * 80)

    # Display each page
    for i, document in enumerate(documents):

        print(f"\nDocument/Page {i+1}")
        print("-" * 80)

        print("Source :", document.metadata["source"])
        print("Page   :", document.metadata["page"] + 1)

        print("\nContent Preview:\n")
        print(document.page_content[:500])
        print("\n" + "=" * 80)


if __name__ == "__main__":
    main()