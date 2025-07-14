from rag_project.core.retriever import retrieve
from rag_project.core.generator import generate

def run_pipeline(query):
    docs = retrieve(query)
    answer = generate(query, docs)
    print("Respuesta final:", answer)
