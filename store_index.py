from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeSparseVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY  = os.getenv("GOOGLE_API_KEY")

os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY 

extracted_data = load_dotenv(data = "data/")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)

embedding = download_embeddings()

pc = Pinecone(api_key= PINECONE_API_KEY)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension= 384,
        metric= "cosine",
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)