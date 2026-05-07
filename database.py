import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session 
from sqlalchemy.dialects.postgresql import ARRAY
from langchain_core.tools import tool

load_dotenv()

class Base(DeclarativeBase):
    pass 

class CompanyDetail(Base):
    __tablename__ = "company_details"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    company_name: Mapped[str] = mapped_column(String(255))
    founded_in: Mapped[Date] = mapped_column(Date, nullable=True)
    founded_by: Mapped[list] = mapped_column(ARRAY(String))

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(url=DATABASE_URL)

@tool
def insert_company(company_name: str, founded_in: str | None, founded_by: list) -> str:
    """Insert a company record into the company_details table in PostgreSQL."""
    
    # Clean up founded_in
    clean_date = None
    if founded_in and founded_in not in ('None', 'null', '(None)', ''):
        clean_date = founded_in
    
    with Session(engine) as session:
        company = CompanyDetail(
            company_name=company_name,
            founded_in=clean_date,
            founded_by=founded_by
        )
        session.add(company)
        session.commit()
    return f"Inserted: {company_name}"
