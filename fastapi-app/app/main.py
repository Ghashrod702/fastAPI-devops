from fastapi import FastAPI
from prometheus_client import Counter, Histogram

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK"}
