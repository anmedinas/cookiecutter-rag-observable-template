from opentelemetry import trace
tracer = trace.get_tracer(__name__)

def retrieve(query):
    with tracer.start_as_current_span("retriever"):
        return [{"text": "Documento simulado"}]
