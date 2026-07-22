from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "data"


def load_documents():
    """
    Load all PDF documents from the data folder.
    """
    loader = PyPDFDirectoryLoader(DATA_PATH)
    return loader.load()


def split_documents(documents):
    """
    Split documents into chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    return splitter.split_documents(documents)


def create_embedding_model():
    """
    Load the embedding model.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )