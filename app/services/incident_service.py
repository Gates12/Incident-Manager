from uuid import UUID, uuid4

from app.repositories.incident_repository import InMemoryIncidentRepository
from app.schemas.incident import Incident, IncidentCreate


class IncidentNotFoundError(Exception):
    pass


class IncidentService:
    def __init__(self, repository: InMemoryIncidentRepository):
        self._repository = repository

    def create_incident(self, payload: IncidentCreate) -> Incident:
        incident = Incident(
            id=uuid4(),
            title=payload.title,
            description=payload.description,
            severity=payload.severity,
            status=payload.status,
        )
        return self._repository.save(incident)

    def list_incidents(self) -> list[Incident]:
        return self._repository.list_all()

    def get_incident(self, incident_id: UUID) -> Incident:
        incident = self._repository.get_by_id(incident_id)

        if incident is None:
            raise IncidentNotFoundError("Incident not found")

        return incident