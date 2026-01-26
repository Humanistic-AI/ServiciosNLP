from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, AI Engineer"}

@app.get("/hello")
def new():
    return {"message": "Hello, Maxi!"}