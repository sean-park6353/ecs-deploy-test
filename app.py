from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "안티티티 프레져"}