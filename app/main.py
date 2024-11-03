from fastapi import FastAPI

app = FastAPI()

#update repo
@app.get("/")
def read_root():
    return {"Hello": "FAST-API in GKE"}

