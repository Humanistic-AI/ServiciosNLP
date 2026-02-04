from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.word_count import router as word_count_router

app = FastAPI(title="Servicios NLP")

app.include_router(health_router)
app.include_router(word_count_router)