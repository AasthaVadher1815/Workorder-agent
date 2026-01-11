from sqlalchemy.orm import Session
from database.models.change_events import ChangeEvent

def insert_change_events(db: Session, run_id, wo_id: str, events: list[dict]):
    for e in events:
        db.add(ChangeEvent(
            run_id=run_id,
            wo_id=wo_id,
            qs_number=e["qs_number"],
            list_field=e.get("list_field"),
            jurisdiction=e.get("jurisdiction"),
            change_type=e["change_type"],
            target=e.get("target"),
            target_identifier=e.get("target_identifier"),
            field_path=e.get("field_path"),
            old_value=e.get("old_value"),
            new_value=e.get("new_value"),
            reason_code=e.get("reason_code"),
            reason=e["reason"],
            evidence_text=e["evidence_text"],
            effective_date=e.get("effective_date"),
            source_document=e.get("source_document"),
        ))
    db.flush()
