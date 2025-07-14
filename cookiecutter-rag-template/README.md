# 🧠 {{ cookiecutter.project_name }}

Proyecto generado con la plantilla Cookiecutter [cookiecutter-rag-observable-template](https://github.com/TU_USUARIO/cookiecutter-rag-observable-template).  
Sistema RAG (Retrieval-Augmented Generation) modular, trazable y monitoreado con observabilidad completa.

---

## ⚙️ Configuración rápida

```bash
# Instala dependencias
pip install -r requirements.txt

# Ejecuta el pipeline
python scripts/run_pipeline.py
```

---

## 📊 Observabilidad

Este proyecto incluye integración con OpenTelemetry + OpenInference + Grafana Tempo.

1. Corre la infraestructura:

```bash
docker compose -f docker/docker-compose.yml up
```

2. Accede a los dashboards:

- Grafana: http://localhost:3000 (admin/admin)
- Prometheus: http://localhost:9090
- Tempo (traces): http://localhost:3200

---

## 📁 Estructura del proyecto

```
{{ cookiecutter.project_slug }}/
├── rag_project/
│   ├── core/              # Componentes RAG: retriever, generator
│   ├── interfaces/        # Adaptadores (LLM, vector store)
│   ├── observability/     # OpenTelemetry setup
│   ├── config/            # Configuración en YAML
├── scripts/
├── docker/
├── notebooks/
├── tests/
├── requirements.txt
├── .env
```

---

## 🔧 Configuración

Revisa el archivo:

```yaml
rag_project/config/base.yaml
```

Para configurar:

- El proveedor de LLM (`{{ cookiecutter.llm_provider }}`)
- El vector store (`{{ cookiecutter.vector_store }}`)

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🧠 Sobre este proyecto

Desarrollado por **{{ cookiecutter.author_name }}**  
Inspirado en buenas prácticas de trazabilidad en RAG y LLMops  
MIT License
