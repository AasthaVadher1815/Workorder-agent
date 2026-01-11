from database.connection import SessionLocal
from database.repositories.work_order_repo import fetch_work_order
from database.repositories.run_repo import create_run, update_run_status
from database.repositories.change_event_repo import insert_change_events
from context.qsid_context_builder import build_qsid_context
from context.context_validator import validate_context

def process_input_snapshot(input_snapshot: dict, wo_id: str, model_name: str) -> str:
    db = SessionLocal()
    try:
        wo = fetch_work_order(db, wo_id)
        if wo is None:
            raise ValueError(f"WO not found: {wo_id}")

        run = create_run(db, wo_id=wo.wo_id, wo_version=wo.version, wo_hash=wo.context_hash, model_name=model_name)
        update_run_status(db, run, "STARTED")

        records = input_snapshot.get("records", [])
        for row in records:
            qs = row.get("QS_Number") or row.get("qs_number") or row.get("QSID") or row.get("QSNumber")
            if not qs:
                continue

            ctx = build_qsid_context(wo.context_json, str(qs))
            validate_context(ctx)

            # TODO: Call LLM Pass1 + validate, then Pass2 + validate.
            events = []

            if events:
                insert_change_events(db, run_id=run.run_id, wo_id=wo.wo_id, events=events)

        update_run_status(db, run, "SUCCESS")
        db.commit()
        return str(run.run_id)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
