from azure.storage.blob import BlobServiceClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SimpleField, SearchIndex
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureCognitiveSearch
import os

# Load documents, split, embed and upload to Cognitive Search
def upload_docs_to_vector_store(file_path, openai_key, search_service_endpoint, index_name):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    vector_store = AzureCognitiveSearch(
        azure_search_endpoint=search_service_endpoint,
        index_name=index_name,
        embedding=embeddings
    )
    vector_store.add_documents(docs)
