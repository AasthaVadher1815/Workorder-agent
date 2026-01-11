import argparse
from database.connection import SessionLocal
from ingestion.wo_loader import load_master_json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    args = ap.parse_args()
    db = SessionLocal()
    try:
        load_master_json(db, args.path)
        db.commit()
        print("Loaded work orders.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
