from fastapi import FastAPI

from app.api.incidents import router as incidents_router

app = FastAPI(title="Incident Manager API")

app.include_router(incidents_router)


@app.get("/")
def read_root():
    return {"message": "Incident Manager API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}