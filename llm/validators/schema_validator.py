from jsonschema import validate

CHANGE_EVENT_SCHEMA = {
  "type": "object",
  "required": ["qs_number", "change_type", "target_identifier", "reason", "evidence_text"],
  "properties": {
    "qs_number": {"type": "string"},
    "change_type": {"type": "string", "enum": ["ADD", "DELETE", "MODIFY"]},
    "target_identifier": {"type": "string"},
    "reason": {"type": "string"},
    "evidence_text": {"type": "string"}
  }
}

OUTPUT_SCHEMA = {
  "type": "object",
  "required": ["changes"],
  "properties": {
    "changes": {"type": "array", "items": CHANGE_EVENT_SCHEMA}
  }
}

def validate_output(obj: dict):
    validate(instance=obj, schema=OUTPUT_SCHEMA)
