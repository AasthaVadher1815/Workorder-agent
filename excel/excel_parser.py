import pandas as pd

def parse_excel_to_snapshot(path: str) -> dict:
    """Parse Excel file and normalize column names"""
    df = pd.read_excel(path)
    
    # Normalize column names - remove spaces and convert to standard format
    df.columns = df.columns.str.strip()
    
    # Rename columns to standard format
    column_mapping = {
        'QS Number': 'QS Number',
        'QS_Number': 'QS Number',
        'QSNumber': 'QS Number',
        'qs number': 'QS Number',
        'qs_number': 'QS Number',
        'qsnumber': 'QS Number',
    }
    
    # Apply column rename (case-insensitive matching)
    for old_col in df.columns:
        for key, value in column_mapping.items():
            if old_col.lower() == key.lower():
                df.rename(columns={old_col: value}, inplace=True)
                break
    
    # Convert to records and clean up None/NaN values
    records = []
    for _, row in df.iterrows():
        record = {}
        for col, val in row.items():
            # Skip NaN values
            if pd.isna(val):
                record[col] = None
            else:
                record[col] = str(val).strip() if isinstance(val, str) else val
        records.append(record)
    
    return {"records": records}
