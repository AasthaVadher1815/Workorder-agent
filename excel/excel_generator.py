from openpyxl import Workbook
from excel.excel_formatting import apply_table_formatting, color_row, normalize_sizes

DEFAULT_HEADERS = [
    "Input_Name","WO_No","QS_Number","List_Field","Jurisdiction",
    "Change_Type","Target","Target_Identifier","Field_Path",
    "Old_Value","New_Value","Reason_Code","Reason","Evidence_Text",
    "Effective_Date","Source_Document"
]

def generate_change_log_xlsx(change_events: list[dict], out_path: str, headers=None):
    headers = headers or DEFAULT_HEADERS
    wb = Workbook()
    ws = wb.active
    ws.title = "Change_Log"
    ws.append(headers)

    for e in change_events:
        ws.append([
            e.get("input_name",""),
            e.get("wo_no",""),
            e.get("qs_number",""),
            e.get("list_field",""),
            e.get("jurisdiction",""),
            e.get("change_type",""),
            e.get("target",""),
            e.get("target_identifier",""),
            e.get("field_path",""),
            e.get("old_value",""),
            e.get("new_value",""),
            e.get("reason_code",""),
            e.get("reason",""),
            e.get("evidence_text",""),
            e.get("effective_date",""),
            e.get("source_document",""),
        ])
        color_row(ws, ws.max_row, e.get("change_type",""))

    apply_table_formatting(ws, headers)
    normalize_sizes(ws, headers)
    wb.save(out_path)
    return out_path
