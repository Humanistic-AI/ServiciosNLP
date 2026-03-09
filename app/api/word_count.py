from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from fastapi import HTTPException   
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

from app.core.word_count import count_words
from app.core.export import export_counts_to_csv

router = APIRouter()
datadir = "/tmp/"




class WordCountRequest(BaseModel):
    text: str

#ToDo cambiar para que maneje file uploads
@router.post("/word-count")
def word_count(req: WordCountRequest):
    request_id = str(uuid.uuid4())

    counts = count_words(req.text)

    filename = datadir + "result_" + request_id + ".csv"
    
    # export_counts_to_csv(counts, filename)
    background_tasks.add_task(export_counts_to_csv, counts, filename)

    return {"request_id": request_id, "message":"regresa más tarde para ver si está tu resultado"}

@router.get("/status/{request_id}")
def get_task_status(request_id: str):
    filename = datadir+"result_" + request_id + ".csv"
    try:
        with open(filename, "r") as fin:
            return {"request_id": request_id, 
                    "status": "completed"}
    except FileNotFoundError:
        return {"request_id": request_id, 
                "status": "pending"}
    
@router.get("/results/{request_id}")
def get_results(request_id: str):
    filename = datadir+"result_" + request_id + ".csv"
    try:        
        return FileResponse(filename, media_type='application/octet-stream',filename=filename)
    except RuntimeError:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
