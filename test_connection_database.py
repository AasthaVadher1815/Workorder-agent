from sqlalchemy import create_engine, text


DATABASE_URL="mysql+pymysql://root:@localhost:3306/workorder_agent"


engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())
