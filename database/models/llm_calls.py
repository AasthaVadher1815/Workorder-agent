from sqlalchemy import Column, Text, Integer, DateTime, String
from sqlalchemy.sql import func
import uuid
from .base import Base

class LLMCall(Base):
    __tablename__ = "llm_calls"
    llm_call_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    run_id = Column(String(36), nullable=False)
    qs_number = Column(Text, nullable=True)
    prompt_hash = Column(Text, nullable=False)
    response_hash = Column(Text, nullable=False)
    tokens_in = Column(Integer, nullable=True)
    tokens_out = Column(Integer, nullable=True)
    model_name = Column(Text, nullable=False)
    temperature = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
