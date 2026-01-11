import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

def get_engine():
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set. Configure it in your environment or .env")
    return create_engine(url, pool_pre_ping=True, connect_args={"charset": "utf8mb4"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
