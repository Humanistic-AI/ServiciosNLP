# ServiciosNLP

![Status](https://badgen.net/badge/status/in%20progress/yellow)
![Python](https://badgen.net/badge/Python/3.12/blue)
![Framework](https://badgen.net/badge/Framework/FastAPI/orange)
![Server](https://badgen.net/badge/Server/Uvicorn/purple)
![Container](https://badgen.net/badge/Container/Docker/cyan)
![VC](https://badgen.net/badge/Version%20Control/GitHub/pink)

ServiciosNLP is an educational backend platform built with **Python** and **FastAPI**.  
The goal of the project is to provide NLP-based services for humanities students, such as word frequency analysis, named entity recognition, and document clustering, through a clean, documented REST API.

The project is designed to grow incrementally, starting with basic text processing and progressively integrating more advanced NLP and AI-based features.

---

## Screenshot
<img width="950" height="882" alt="Word Counter" src="https://github.com/user-attachments/assets/679cc190-b5c4-49a9-8b14-7c8cf6a23130" />


---

## Features & Stack

- REST API built with **FastAPI**
- Automatic interactive documentation via **Swagger UI**
- Word frequency analysis with Spanish stopword filtering and text normalization
- Results exported as downloadable **CSV files**
- Asynchronous task handling using **BackgroundTasks**
- Fully containerized with **Docker**
- Deployable to any machine with Docker installed
- Version-controlled with **Git & GitHub** using feature branches and pull requests

---

## Highlighted Technical Detail

The word count service processes text asynchronously: when a request arrives, the API responds immediately with a unique `request_id` while the CSV export runs in the background. The client can then poll a `/status/{request_id}` endpoint and download the result via `/results/{request_id}` once it's ready.

This pattern simulates a real-world async job queue and demonstrates FastAPI's dependency injection system, where framework-managed objects like `BackgroundTasks` are automatically provided to route handlers when declared as parameters.

---

## Concepts Explored

- Building modular REST APIs with **FastAPI routers**
- Input validation and schema definition using **Pydantic**
- Asynchronous background task execution with **BackgroundTasks**
- Dependency injection in FastAPI
- Text normalization and Spanish stopword filtering with **regex**
- CSV export from Python dictionaries
- Containerization with **Docker** and hot reload in development
- Remote server deployment with Docker
- Git branching workflow with feature branches and pull requests

---

## Project Structure
```bash
app/
├── main.py              → FastAPI entry point, router registration
├── api/
│   ├── health.py        → Health check endpoint
│   └── word_count.py    → Word count endpoints (POST, GET status, GET results)
└── core/
    ├── word_count.py    → NLP logic: normalization, stopword filtering, counting
    └── export.py        → CSV export utility
```

---

## Getting Started

### Requirements

- Python 3.12+
- Docker (optional, recommended)

### Run locally with Uvicorn
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server with auto-reload
uvicorn app.main:app --reload
```

Open in your browser:
- App: `http://127.0.0.1:8000`
- API docs: `http://127.0.0.1:8000/docs`

### Run with Docker (development mode)
```bash
# Build the image
docker build -t nlpservices .

# Run with hot reload
docker run --rm -p 8000:80 -v ./app:/code/app -it nlpservices
```

### Run with Docker (production-like mode)
```bash
docker run --rm -p 8000:80 nlpservices
```

### Deploy to a remote server

This project is fully containerized and can be deployed to any machine with Docker installed. Clone the repository, build the image, and run the container exposing the desired port.

---

## Roadmap

- [x] Project structure with FastAPI routers
- [x] Health check endpoint
- [x]  Word count service with CSV export and async processing
- [ ]  Basic Named Entity Recognition (NER)
- [ ] Document clustering
- [ ] Sentence classification
- [ ] Paragraph clustering
- [ ] File upload support (TXT, PDF)
- [ ] LLM integration

---

## Contact

- [GitHub](https://github.com/franciscoxcode)
- [LinkedIn](https://www.linkedin.com/in/franciscoxcode/)
- [Email](mailto:fxcasillas.dev@gmail.com)

---

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE).
