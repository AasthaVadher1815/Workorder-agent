from sqlalchemy import Column, Text, DateTime, String
from sqlalchemy.sql import func
import uuid
from .base import Base

class InputFile(Base):
    __tablename__ = "input_files"
    input_file_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    wo_id = Column(Text, nullable=False)
    original_filename = Column(Text, nullable=False)
    storage_uri = Column(Text, nullable=False)
    file_hash = Column(Text, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
