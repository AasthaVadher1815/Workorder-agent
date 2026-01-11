from sqlalchemy import Column, Text, Integer, DateTime, String
from sqlalchemy.sql import func
import uuid
from .base import Base

class Run(Base):
    __tablename__ = "runs"
    run_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    wo_id = Column(Text, nullable=False)
    wo_version = Column(Integer, nullable=False)
    wo_context_hash = Column(Text, nullable=False)
    input_file_id = Column(String(36), nullable=True)
    model_name = Column(Text, nullable=False)
    status = Column(Text, nullable=False, default="STARTED")
    error_message = Column(Text, nullable=True)
    started_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    finished_at = Column(DateTime(timezone=True), nullable=True)
