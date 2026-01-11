from sqlalchemy import Column, Text, DateTime, String
from sqlalchemy.sql import func
import uuid
from .base import Base

class RunArtifact(Base):
    __tablename__ = "run_artifacts"
    artifact_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    run_id = Column(String(36), nullable=False)
    artifact_type = Column(Text, nullable=False)
    storage_uri = Column(Text, nullable=False)
    artifact_hash = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
