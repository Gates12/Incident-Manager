from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Incident Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}