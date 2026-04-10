from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid

from app.core.sentence_classification import process_text

router = APIRouter()
datadir = "/tmp/"


class SentenceClassificationRequest(BaseModel):
    text: str
    categories: list[str]
    examples: str


@router.post("/")
def classify(req: SentenceClassificationRequest, background_tasks: BackgroundTasks):
    request_id = str(uuid.uuid4())
    filename = datadir + "result_" + request_id + ".xlsx"

    background_tasks.add_task(process_text, req.text, req.categories, req.examples, filename)

    return {"request_id": request_id, "message": "Processing your request, come back later"}


@router.get("/status/{request_id}")
def get_status(request_id: str):
    import os
    filename = datadir + "result_" + request_id + ".xlsx"
    if os.path.exists(filename):
        return {"request_id": request_id, "status": "completed"}
    return {"request_id": request_id, "status": "pending"}


@router.get("/results/{request_id}")
def get_results(request_id: str):
    filename = datadir + "result_" + request_id + ".xlsx"
    try:
        return FileResponse(filename, media_type='application/octet-stream', filename=filename)
    except RuntimeError:
        raise HTTPException(status_code=404, detail="Result not found")