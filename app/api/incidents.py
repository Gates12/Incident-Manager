from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.repositories.incident_repository import InMemoryIncidentRepository
from app.schemas.incident import Incident, IncidentCreate
from app.services.incident_service import IncidentNotFoundError, IncidentService

router = APIRouter(prefix="/incidents", tags=["incidents"])

repository = InMemoryIncidentRepository()
service = IncidentService(repository)


@router.post("/", response_model=Incident, status_code=status.HTTP_201_CREATED)
def create_incident(payload: IncidentCreate):
    return service.create_incident(payload)


@router.get("/", response_model=list[Incident])
def list_incidents():
    return service.list_incidents()


@router.get("/{incident_id}", response_model=Incident)
def get_incident(incident_id: UUID):
    try:
        return service.get_incident(incident_id)
    except IncidentNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error