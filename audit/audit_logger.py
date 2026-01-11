import json
from storage.file_hashing import sha256_text

def hash_json(obj: dict) -> str:
    return sha256_text(json.dumps(obj, sort_keys=True, ensure_ascii=False))
