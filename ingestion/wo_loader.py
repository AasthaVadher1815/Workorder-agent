import json
from pathlib import Path
from sqlalchemy.orm import Session
from ingestion.wo_normalizer import normalize_work_order
from database.repositories.work_order_repo import upsert_work_order

def load_master_json(db: Session, master_path: str):
    data = json.loads(Path(master_path).read_text(encoding="utf-8"))

    items = []
    
    if isinstance(data, dict):
        # Handle nested structure: {query_key: [list of records]}
        for key, value in data.items():
            if isinstance(value, list):
                # Value is a list of work orders
                items.extend(value)
            elif isinstance(value, dict):
                # Value is a single work order dict
                if "wo_id" not in value:
                    value["wo_id"] = key
                items.append(value)
    elif isinstance(data, list):
        items = data
    else:
        raise ValueError("Unsupported master JSON shape. Expected dict or list.")

    for wo in items:
        norm = normalize_work_order(wo)
        wo_id = norm.get("wo_id") or norm.get("WO_No") or norm.get("Work Order No")
        if not wo_id:
            raise ValueError(f"Work order missing wo_id field after normalization: {wo}")
        upsert_work_order(db, wo_id=str(wo_id), context_json=norm)
