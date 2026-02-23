from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from fastapi import HTTPException   
from fastapi.responses import FileResponse

from core.word_count import count_words

router = APIRouter()
datadir = "/tmp/"

#ToDo: que los resultados se regresen en CSV
#ToDo: que los resultados vengan ordenados del más frecuente, al menos frcuente
#ToDo: que se quiten los signos de puntuación, y que se manejen mayúsculas y minúsculas como iguales
#ToDo: quitar las stopswords

class WordCountRequest(BaseModel):
    text: str

def save_result(request_id: str, resultado, filetype: str):
    filename = datadir+"result_" + request_id + "." + filetype
    if filetype == "json":
        resultado_str = str(resultado)
        with open(filename, "w") as fout:
            fout.write(resultado_str)
    return filename

#ToDo cambiar para que maneje file uploads
@router.post("/word-count")
def word_count(req: WordCountRequest):
    request_id = str(uuid.uuid4())

    json_counts = count_words(req.text)
    save_result(request_id, json_counts, "json")

    return {"request_id": request_id, "message":"regresa más tarde para ver si está tu resultado"}

@router.get("/status/{request_id}")
def get_task_status(request_id: str):
    filename = datadir+"result_" + request_id + ".json"
    try:
        with open(filename, "r") as fin:
            return {"request_id": request_id, 
                    "status": "completed"}
    except FileNotFoundError:
        return {"request_id": request_id, 
                "status": "pending"}
    
@router.get("/results/{request_id}")
def get_results(request_id: str):
    filename = datadir+"result_" + request_id + ".json"
    try:        
        return FileResponse(filename, media_type='application/octet-stream',filename=filename)
    except RuntimeError:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    