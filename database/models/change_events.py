from sqlalchemy import Column, Text, Date, DateTime, String
from sqlalchemy.sql import func
import uuid
from .base import Base

class ChangeEvent(Base):
    __tablename__ = "change_events"
    change_event_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    run_id = Column(String(36), nullable=False)
    wo_id = Column(Text, nullable=False)
    qs_number = Column(Text, nullable=False)
    list_field = Column(Text, nullable=True)
    jurisdiction = Column(Text, nullable=True)
    change_type = Column(Text, nullable=False)
    target = Column(Text, nullable=True)
    target_identifier = Column(Text, nullable=True)
    field_path = Column(Text, nullable=True)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    reason_code = Column(Text, nullable=True)
    reason = Column(Text, nullable=False)
    evidence_text = Column(Text, nullable=False)
    effective_date = Column(Date, nullable=True)
    source_document = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
