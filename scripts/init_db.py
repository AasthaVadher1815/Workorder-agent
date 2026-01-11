from database.connection import get_engine
from database.models.base import Base

# Import models so SQLAlchemy knows about them
from database.models.work_orders import WorkOrder, WorkOrderHistory
from database.models.runs import Run
from database.models.input_files import InputFile
from database.models.run_artifacts import RunArtifact
from database.models.change_events import ChangeEvent
from database.models.llm_calls import LLMCall


def main():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")


if __name__ == "__main__":
    main()
