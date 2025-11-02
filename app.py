from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "아니, 윈터가 더예뻐"}