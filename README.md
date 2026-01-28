# ServiciosNLP

ServiciosNLP is an educational backend platform built with **Python** and **FastAPI**.  
The goal of the project is to provide simple NLP-related services for humanities students, such as document processing and text analysis, through a web-based API.

This project is developed as part of an academic practice and is designed to grow incrementally, starting with basic text processing services and later integrating more advanced NLP and AI-based features.

## Tech Stack

- Python 3
- FastAPI
- Uvicorn (ASGI server)
- JSON-based APIs
- Git & GitHub

## Project Structure

ServiciosNLP/
├── app/
│   ├── init.py
│   └── main.py
├── .gitignore
├── README.md
├── requirements.txt

---

## How to Run the Project

### Development mode

Runs the server with auto-reload enabled (recommended during development):
`uvicorn app.main:app --reload`

Once running, open your browser at: 
`http://127.0.0.1:8000`

API documentation (Swagger UI):
`http://127.0.0.1:8000/docs`

### Production-like mode

Runs the server exposed to the network (no auto-reload):
`uvicorn app.main:app --host 0.0.0.0`

## Current Features

- Basic FastAPI application
- Example GET endpoints
- Automatic API documentation with Swagger UI

## Roadmap (Work in progress)

- Text processing services (word count, frequency analysis)
- NLP-based services (classification, clustering, NER)
- File uploads (TXT, PDF)
- Export results as Excel files
- Optional AI integration using LLM APIs
- Web-based user interface