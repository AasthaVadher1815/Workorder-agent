# Workorder Agent (Scaffold)

This repository scaffolds an agentic pipeline that:
- Stores Work Orders (WO) as JSONB in Postgres (versioned + hashed)
- Accepts Excel inputs (variable columns)
- Filters WO context per QSID
- Uses an LLM in two passes (extract changes, then write reasons)
- Generates an output Excel (color coded + normal sizing)
- Writes full audit artifacts and run logs

## Quickstart
1) Create and activate a virtualenv
2) `pip install -r requirements.txt`
3) Copy `.env.example` to `.env` and fill values
4) Run:
   - `python -m scripts.load_master_wo_json --help`
   - `python -m scripts.process_excel_local --help`

## Notes
- This is a scaffold: functions include TODO markers where your org-specific logic will go.
- All artifacts (input JSON, filtered context, prompts/responses, output JSON, output XLSX) are designed to be saved for audit and future fine-tuning.
