from sqlalchemy.orm import Session
from database.models.run_artifacts import RunArtifact

def add_artifact(db: Session, run_id, artifact_type: str, storage_uri: str, artifact_hash: str) -> RunArtifact:
    art = RunArtifact(
        run_id=run_id,
        artifact_type=artifact_type,
        storage_uri=storage_uri,
        artifact_hash=artifact_hash,
    )
    db.add(art)
    db.flush()
    return art
