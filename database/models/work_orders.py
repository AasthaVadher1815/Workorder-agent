from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import JSON
from sqlalchemy.sql import func
from .base import Base

class WorkOrder(Base):
    __tablename__ = "work_orders"
    wo_id = Column(String(50), primary_key=True)
    version = Column(Integer, nullable=False, default=1)
    context_json = Column(JSON, nullable=False)
    context_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class WorkOrderHistory(Base):
    __tablename__ = "work_orders_history"
    wo_id = Column(String(50), primary_key=True)
    version = Column(Integer, primary_key=True)
    context_json = Column(JSON, nullable=False)
    context_hash = Column(String(255), nullable=False)
    archived_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
