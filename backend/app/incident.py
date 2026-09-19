from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str
    service: str
    severity: str
    symptoms: list[str]


class IncidentResponse(Incident):
    id: int

    model_config = {
        "from_attributes": True
    }