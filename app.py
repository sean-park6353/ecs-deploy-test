from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "카리나 예쁘다"}