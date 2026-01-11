def ensure_evidence_present(evidence_text: str):
    if not evidence_text or len(evidence_text.strip()) < 10:
        raise ValueError("Evidence text missing or too short")
