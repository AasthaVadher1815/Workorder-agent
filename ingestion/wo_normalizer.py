def normalize_work_order(raw: dict) -> dict:
    """Normalize WO JSON to an agent-friendly schema.
    Maps fields from work_orders_master.json format to internal schema.
    """
    # Map incoming field names to our schema
    normalized = {
        "wo_id": raw.get("WO_No") or raw.get("Work Order No") or raw.get("wo_id"),
        "wo_version": raw.get("Version", 1),
        "products": raw.get("Products", ""),
        "qs_number": raw.get("QS Number") or raw.get("qs_number"),
        "jurisdiction": raw.get("Jurisdiction", ""),
        "researcher_status": raw.get("Researcher Status", ""),
        "general_instructions": raw.get("General Instructions", ""),
        "regulatory_background": raw.get("Regulatory Background", ""),
        "short_name": raw.get("Short Name", ""),
        "cra_user": raw.get("CraUser", ""),
        "cra_wo_status": raw.get("CraWoStatus", ""),
        "cra_priority": raw.get("CraPriority"),
        "client": raw.get("Client", ""),
        "cra_notes": raw.get("CraNotes", ""),
        "modified_date": raw.get("ModifiedDate"),
        "created_by": raw.get("CreatedBy", ""),
        "list_field": raw.get("ListField", ""),
        "production_date": raw.get("ProductionDate"),
        "topics": raw.get("Topics", ""),
        "modules": raw.get("Modules", ""),
        "primary_researcher": raw.get("PrimaryResearcher", ""),
        "secondary_db_researcher": raw.get("SecondaryDbResearcher", ""),
        "submit_date": raw.get("SubmitDate"),
        "revision_date": raw.get("RevisionDate"),
        "list_status": raw.get("ListStatus", ""),
        "wo2prod": raw.get("WO2Prod"),
        "pub2prod": raw.get("Pub2Prod"),
        "pub2wo": raw.get("Pub2Wo"),
    }
    
    # Remove None values for cleaner data
    return {k: v for k, v in normalized.items() if v is not None}
