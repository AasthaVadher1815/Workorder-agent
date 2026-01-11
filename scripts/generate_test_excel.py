#!/usr/bin/env python
"""Generate sample Excel file from loaded work orders for testing."""

import pandas as pd
from database.connection import SessionLocal
from database.models.work_orders import WorkOrder

def generate_test_excel_from_wo(wo_id: str, output_file: str = "test_changes.xlsx"):
    """Generate test Excel with sample changes for a work order."""
    db = SessionLocal()
    
    # Get work order
    wo = db.query(WorkOrder).filter(WorkOrder.wo_id == str(wo_id)).first()
    if not wo:
        print(f"❌ Work order {wo_id} not found")
        return
    
    # Get QS Number from context if available
    qs_number = "QSAPA67"  # Default
    if isinstance(wo.context_json, dict):
        qs_number = wo.context_json.get("qs_number", qs_number)
    
    # Create sample change data
    data = {
        'QS Number': [qs_number] * 5,
        'Work Order No': [str(wo_id)] * 5,
        'Change Type': ['Update', 'Add', 'Delete', 'Update', 'Add'],
        'Target': ['Substance List', 'CAS Number', 'Classification', 'Health Hazard', 'Physical Hazard'],
        'Old Value': ['Old substance', None, 'Class A', 'Not specified', None],
        'New Value': ['New substance', '120928-09-8', 'Class B', 'Acute Toxicity', 'Reactive'],
        'Reason': [
            'Regulatory update',
            'New substance added',
            'Classification revision',
            'Updated hazard assessment',
            'New physical hazard identified'
        ],
    }
    
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"✅ Created {output_file}")
    print(f"   Work Order: {wo_id}")
    print(f"   QS Number: {qs_number}")
    print(f"   Rows: {len(df)}")
    print(f"\n   Use: python -m scripts.process_excel_local --excel {output_file} --wo-id {wo_id}")
    
    db.close()

if __name__ == "__main__":
    # Generate for the work order we tested earlier
    generate_test_excel_from_wo("10479", "test_changes_10479.xlsx")
    
    # Or generate for another work order
    # generate_test_excel_from_wo("10478", "test_changes_10478.xlsx")
