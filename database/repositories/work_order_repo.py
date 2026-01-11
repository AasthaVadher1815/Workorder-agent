import hashlib
import json
from sqlalchemy.orm import Session
from database.models.work_orders import WorkOrder, WorkOrderHistory

def canonical_json(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def upsert_work_order(db: Session, wo_id: str, context_json: dict) -> WorkOrder:
    canon = canonical_json(context_json)
    h = sha256_text(canon)

    existing = db.get(WorkOrder, wo_id)
    if existing is None:
        wo = WorkOrder(wo_id=wo_id, version=1, context_json=context_json, context_hash=h)
        db.add(wo)
        db.flush()
        return wo

    if existing.context_hash == h:
        return existing

    db.add(WorkOrderHistory(
        wo_id=existing.wo_id,
        version=existing.version,
        context_json=existing.context_json,
        context_hash=existing.context_hash
    ))

    existing.version += 1
    existing.context_json = context_json
    existing.context_hash = h
    db.add(existing)
    db.flush()
    return existing

def fetch_work_order(db: Session, wo_id: str) -> WorkOrder | None:
    return db.get(WorkOrder, wo_id)
