from opentelemetry import trace
tracer = trace.get_tracer(__name__)

def generate(query, documents):
    with tracer.start_as_current_span("generator"):
        return f"Respuesta simulada con contexto: {documents[0]['text']}"
