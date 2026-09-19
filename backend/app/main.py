from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.incident import Incident, IncidentResponse
from backend.app.models import IncidentDB


app = FastAPI(
    title="AegisOps API",
    description="AI-powered cloud operations and responsible AI governance platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AegisOps API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/incidents",
    response_model=IncidentResponse,
    status_code=201,
)
def create_incident(
    incident: Incident,
    db: Session = Depends(get_db),
):
    incident_db = IncidentDB(
        incident_id=incident.incident_id,
        service=incident.service,
        severity=incident.severity,
        symptoms=incident.symptoms,
    )

    db.add(incident_db)
    db.commit()
    db.refresh(incident_db)

    return incident_db


@app.get(
    "/incidents",
    response_model=list[IncidentResponse],
)
def get_incidents(
    db: Session = Depends(get_db),
):
    statement = select(IncidentDB)

    incidents = db.scalars(statement).all()

    return incidents


@app.get(
    "/incidents/{incident_id}",
    response_model=IncidentResponse,
)
def get_incident(
    incident_id: str,
    db: Session = Depends(get_db),
):
    statement = select(IncidentDB).where(
        IncidentDB.incident_id == incident_id
    )

    incident = db.scalars(statement).first()

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident