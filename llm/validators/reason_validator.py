FORBIDDEN = ["WO_", "GENERAL_INSTRUCTION", "Reason_Code"]

def validate_reason(reason: str):
    for s in FORBIDDEN:
        if s in reason:
            raise ValueError(f"Reason contains forbidden token: {s}")
