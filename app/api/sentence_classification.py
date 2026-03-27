from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid

from app.core.sentence_classification import process_text

router = APIRouter()
datadir = "/tmp/"


class ClassRequest(BaseModel):
    nombre: str
    descripcion: str
    ejemplos: str


class SentenceClassificationRequest(BaseModel):
    text: str
    clases: list[ClassRequest]

@router.post("/sentence-classification")
def classify(req: SentenceClassificationRequest, background_tasks: BackgroundTasks):
    request_id = str(uuid.uuid4())
    filename = datadir + "result_" + request_id + ".xlsx"
    
    clases_dict = [c.model_dump() for c in req.clases]
    
    background_tasks.add_task(process_text, req.text, clases_dict, filename)
    
    return {"request_id": request_id, "message": "Processing your request, come back later"}

@router.get("/sentence-classification/status/{request_id}")
def get_status(request_id: str):
    filename = datadir + "result_" + request_id + ".xlsx"
    try:
        with open(filename, "r") as fin:
            return {"request_id": request_id, "status": "completed"}
    except FileNotFoundError:
        return {"request_id": request_id, "status": "pending"}


@router.get("/sentence-classification/results/{request_id}")
def get_results(request_id: str):
    filename = datadir + "result_" + request_id + ".xlsx"
    try:
        return FileResponse(filename, media_type='application/octet-stream', filename=filename)
    except RuntimeError:
        raise HTTPException(status_code=404, detail="Result not found")