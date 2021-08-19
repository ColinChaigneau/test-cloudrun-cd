from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello from Cloud Run CD"


@app.get("/another")
def another_end_point():
    return "Hello from another end point"
