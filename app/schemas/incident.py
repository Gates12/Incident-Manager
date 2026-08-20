from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class IncidentStatus(str, Enum):
    OPEN = "open"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"


class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=1000)
    severity: Severity
    status: IncidentStatus = IncidentStatus.OPEN


class Incident(BaseModel):
    id: UUID
    title: str
    description: str
    severity: Severity
    status: IncidentStatus