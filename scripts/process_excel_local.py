import argparse
import os
from excel.excel_parser import parse_excel_to_snapshot
from agent.orchestrator import process_input_snapshot

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--excel", required=True)
    ap.add_argument("--wo-id", required=True)
    ap.add_argument("--model", default=os.environ.get("LLM_MODEL","gpt-4.1-mini"))
    args = ap.parse_args()

    snap = parse_excel_to_snapshot(args.excel)
    run_id = process_input_snapshot(snap, wo_id=args.wo_id, model_name=args.model)
    print({"run_id": run_id})

if __name__ == "__main__":
    main()
