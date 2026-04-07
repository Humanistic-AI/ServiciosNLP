![Status](https://badgen.net/badge/status/in%20progress/yellow)
![Python](https://badgen.net/badge/Python/3.12/blue)
![Framework](https://badgen.net/badge/Framework/FastAPI/orange)
![Server](https://badgen.net/badge/Server/Uvicorn/purple)
![Container](https://badgen.net/badge/Container/Docker/cyan)
![VC](https://badgen.net/badge/Version%20Control/GitHub/pink)

# ServiciosNLP

ServiciosNLP is an educational backend platform built with **Python** and **FastAPI**.

It provides NLP-based services for humanities researchers — including word frequency analysis, sentence classification, and document clustering — through a clean, documented REST API.

The project grows incrementally, starting with basic text processing and progressively integrating LLM-powered features via the OpenAI API.

---

## Features & stack

- REST API built with **FastAPI**
- Interactive API documentation via **Swagger UI**
- Word frequency analysis with Spanish stopword filtering and text normalization
- Sentence classification powered by **OpenAI GPT** using dynamic system/user prompts
- User-defined classification categories with few-shot examples
- Results exported as downloadable **CSV** and **Excel (.xlsx)** files
- Asynchronous task handling using FastAPI's **BackgroundTasks**
- Fully containerized with **Docker**
- Version-controlled with **Git & GitHub** using feature branches and pull requests

---

## Highlighted technical details

### Async job pattern

When a request arrives, the API responds immediately with a unique `request_id` while the export runs in the background. The client polls `/status/{request_id}` and downloads the result from `/results/{request_id}` when ready. This simulates a real-world async job queue using FastAPI's dependency injection system.

### LLM-powered sentence classification

The classification service builds prompts dynamically at runtime. The **system prompt** defines the model's role and injects the user-defined categories. The **user prompt** provides the sentences and enforces a strict JSON response format. This separation follows best practices for structured LLM output and enables flexible, user-driven classification without redeploying the service.

---

## Concepts explored

- Building modular REST APIs with FastAPI routers
- Input validation and schema definition with Pydantic
- Asynchronous background task execution with BackgroundTasks
- Dependency injection in FastAPI
- Text normalization and Spanish stopword filtering with regex
- Dynamic prompt construction for LLM APIs (system/user prompt separation)
- Structured JSON output enforcement with OpenAI
- CSV and Excel export from Python data structures
- Containerization with Docker and hot reload in development
- Environment variable management with `.env` files
- Git branching workflow with feature branches and pull requests

---

## Project structure

```bash
app/
├── main.py                        → FastAPI entry point, router registration
├── api/
│   ├── health.py                  → Health check endpoint
│   ├── word_count.py              → Word count endpoints (POST, GET status, GET results)
│   └── sentence_classification.py → Sentence classification endpoints
└── core/
    ├── word_count.py              → NLP logic: normalization, stopword filtering, counting
    ├── sentence_classification.py → LLM prompt construction and classification logic
    └── export.py                  → CSV and Excel export utilities
```

---

## Requirements

- Python 3.12+
- Docker (optional, recommended)
- An **OpenAI account** with a valid API key (required for sentence classification)
- A `.env` file in the project root (see below)

---

## Environment setup

This project requires a `.env` file at the root of the project to configure the OpenAI API key. This file is excluded from version control via `.gitignore` to protect sensitive credentials.

> **Never commit your `.env` file to version control.** It contains secret keys that must remain private.

### 1. Create your .env file

In the project root, create a file named `.env` with the following content:

```env
OPENAI_API_KEY=your-api-key-here
```

Refer to `.env_example` (included in the repository) for the expected format.

### 2. Get your OpenAI API key

- Create an account at [platform.openai.com](https://platform.openai.com)
- Navigate to **API Keys** and generate a new key
- Paste the key into your `.env` file

> The sentence classification service will not function without a valid API key. All other services (word count, health check) work without it.

---

## Getting started

### Run locally with Uvicorn

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open in your browser:

- App: `http://127.0.0.1:8000`
- API docs: `http://127.0.0.1:8000/docs`

### Run with Docker — development (hot reload)

```bash
docker build -t nlpservices .
docker run --rm -p 8000:80 -v ./app:/code/app --env-file .env -it nlpservices
```

### Run with Docker — production

```bash
docker run --rm -p 8000:80 --env-file .env nlpservices
```

> The `--env-file .env` flag injects your environment variables into the container at runtime, so secrets never get baked into the Docker image.

---

## Deploy to a remote server

This project is fully containerized. Clone the repository on any machine with Docker installed, add your `.env` file, build the image, and run the container exposing the desired port.

---

## Roadmap

- [x] Project structure with FastAPI routers
- [x] Health check endpoint
- [x] Word count service with CSV export and async processing
- [x] Sentence classification with OpenAI and Excel export
- [ ] Named Entity Recognition (NER)
- [ ] Document clustering
- [ ] Paragraph clustering
- [ ] File upload support (TXT, PDF)

---

## Contact

- [GitHub](https://github.com/franciscoxcode)
- [LinkedIn](https://www.linkedin.com/in/franciscoxcode/)
- [Email](mailto:fxcasillas.dev@gmail.com)

---

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE).
