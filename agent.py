from app.retriever import retrieve_documents
from app.generator import generate_response

def run_agent(query: str) -> str:
    context = retrieve_documents(query)
    response = generate_response(query, context)
    return response
