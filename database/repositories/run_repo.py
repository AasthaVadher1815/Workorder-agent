from sqlalchemy.orm import Session
from database.models.runs import Run

def create_run(db: Session, wo_id: str, wo_version: int, wo_hash: str, model_name: str, input_file_id=None) -> Run:
    run = Run(
        wo_id=wo_id,
        wo_version=wo_version,
        wo_context_hash=wo_hash,
        model_name=model_name,
        input_file_id=input_file_id,
    )
    db.add(run)
    db.flush()
    return run

def update_run_status(db: Session, run: Run, status: str, error_message: str | None = None):
    run.status = status
    run.error_message = error_message
    db.add(run)
    db.flush()
