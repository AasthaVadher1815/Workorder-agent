from pathlib import Path

class ObjectStore:
    def __init__(self, driver: str = "local", base_path: str = "./_object_store"):
        self.driver = driver
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def put_bytes(self, rel_path: str, data: bytes) -> str:
        p = self.base_path / rel_path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return f"file://{p.resolve()}"

    def put_text(self, rel_path: str, text: str, encoding: str = "utf-8") -> str:
        return self.put_bytes(rel_path, text.encode(encoding))
