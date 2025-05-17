from langchain_core.document_loaders import PyMuPDFLoader
from langchain_core.documents.base import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings

class Qdrant:
    def __init__ (self , qdrant_url: str, qdrant_index_name: str):
        self.qdrant_url = qdrant_url
        self.qdrant_index_name = qdrant_index_name
        


async def pdf_to_text(file_path: str, qdrant_url: str, qdrant_index_name: str) -> None:
    # Load the PDF file
    loader = PyMuPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    # Split the text into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(pages)

    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(openai_api_key="your_openai_api_key")

    # Load data into Redis vector store
    vector_store = qdrant.from_documents(
        documents=documents,
        embedding=embeddings,
        redis_url=qdrant_url,
        index_name=qdrant_index_name
    )

    print(f"Data successfully loaded into Redis index: {qdrant_index_name}")