from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database import Base


class IncidentDB(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    service: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    symptoms: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False,
    )