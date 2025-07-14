# 🧠 Cookiecutter RAG Observable Template

Plantilla profesional para construir sistemas **RAG (Retrieval-Augmented Generation)** modulares, trazables y listos para producción, con integración nativa a **OpenTelemetry + OpenInference** y visualización mediante **Grafana, Prometheus y Tempo**.

> ⚙️ Ideal para proyectos de LLMs, agentes, multiagentes y pipelines dinámicos que requieran monitoreo, depuración y extensibilidad.

---

## 🚀 ¿Qué incluye esta plantilla?

- 🔍 Arquitectura RAG modular (`retriever`, `generator`, `planner`, `critic`, etc.)
- 🧩 Instrumentación estándar con [OpenInference](https://github.com/openinference/specification)
- 📊 Visualización con [Grafana](https://grafana.com/), [Tempo](https://grafana.com/oss/tempo/), [Prometheus](https://prometheus.io/)
- 📦 Separación clara entre `core`, `infraestructura`, `interfaces`, `observabilidad`, `config`
- ⚡ Compatible con LLMs de OpenAI, Claude, HuggingFace, etc.
- 🧪 Ready para testing y desarrollo local
- 🐳 Docker-ready (Grafana stack)

---

## 📦 Requisitos

- Python 3.9+
- [Docker + Docker Compose](https://docs.docker.com/compose/)
- [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html)

```bash
pip install cookiecutter
```