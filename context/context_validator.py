def validate_context(ctx: dict):
    if not ctx.get("wo_id"):
        raise ValueError("Context missing wo_id")
    if not ctx.get("qs_number"):
        raise ValueError("Context missing qs_number")
