def build_qsid_context(work_order_json: dict, qs_number: str) -> dict:
    ctx = {
        "wo_id": work_order_json.get("wo_id") or work_order_json.get("WO_No") or work_order_json.get("Work Order No"),
        "qs_number": qs_number,
        "metadata": work_order_json.get("metadata", {}),
        "lists": work_order_json.get("lists", []),
        "general_instructions": work_order_json.get("general_instructions") or work_order_json.get("General Instructions", ""),
        "regulatory_background": work_order_json.get("regulatory_background") or work_order_json.get("Regulatory Background", ""),
        "jurisdiction": work_order_json.get("Jurisdiction", ""),
        "products": work_order_json.get("Products", ""),
        "short_name": work_order_json.get("Short Name", ""),
        "attachments": work_order_json.get("attachments", []),
    }

    gi = ctx.get("general_instructions", [])
    filtered = []
    
    # Handle both list and string formats
    if isinstance(gi, list):
        for ins in gi:
            text = ins.get("text","") if isinstance(ins, dict) else str(ins)
            if qs_number in text:
                filtered.append(ins)
    elif isinstance(gi, str):
        # If it's a string, check if qs_number is mentioned
        if qs_number in gi:
            filtered.append(gi)
    
    ctx["general_instructions_scoped"] = filtered if filtered else gi
    return ctx
