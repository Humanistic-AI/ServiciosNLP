from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.api.word_count import router as word_count_router
from app.api.sentence_classification import router as sentence_classification_router

app = FastAPI(title="Servicios NLP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(word_count_router, prefix="/word-count")
app.include_router(sentence_classification_router, prefix="/sentence-classification")