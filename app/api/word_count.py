from fastapi import APIRouter
from pydantic import BaseModel

from core.word_count import count_words

router = APIRouter()


class WordCountRequest(BaseModel):
    text: str


@router.post("/word-count")
def word_count(req: WordCountRequest):
    return count_words(req.text)