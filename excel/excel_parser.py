import pandas as pd

def parse_excel_to_snapshot(path: str) -> dict:
    df = pd.read_excel(path)
    return {"records": df.to_dict(orient="records")}
