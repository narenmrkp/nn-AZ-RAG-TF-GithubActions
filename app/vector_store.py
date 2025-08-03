from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureCognitiveSearch

def get_vector_store():
    embeddings = OpenAIEmbeddings(
        openai_api_key="<your_openai_key>",
        deployment="embedding"
    )
    return AzureCognitiveSearch(
        azure_search_endpoint="https://ragsearch.search.windows.net",
        index_name="docs-index",
        embedding=embeddings,
        api_key="<your_search_api_key>"
    )