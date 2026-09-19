from backend.app.database import Base, engine
from backend.app.models import IncidentDB


Base.metadata.create_all(engine)

print("Database tables created")