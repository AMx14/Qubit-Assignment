from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the base class for models
Base = declarative_base()

class Company(Base):
    """Represents the existing companies table."""
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_linkedin_url = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Company(company_id={self.company_id}, company_linkedin_url='{self.company_linkedin_url}')>"

class EnrichedCompany(Base):
    """Represents the enriched companies table."""
    __tablename__ = 'enriched_companies'

    company_id = Column(Integer, primary_key=True)
    company_name = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    industry = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    employee_count = Column(Integer, nullable=True)
    employee_count_range = Column(String(50), nullable=True)
    tagline = Column(String(255), nullable=True)
    follower_count = Column(Integer, nullable=True)
    logo_url = Column(String(255), nullable=True)
    cover_image_url = Column(String(255), nullable=True)
    original_cover_image_url = Column(String(255), nullable=True)
    hashtag = Column(String(255), nullable=True)
    locations = Column(Text, nullable=True)
    call_to_action = Column(Text, nullable=True)
    specialities = Column(Text, nullable=True)
    crunchbase_funding_data = Column(Text, nullable=True)
    affiliated_organizations_by_employees = Column(Text, nullable=True)
    affiliated_organizations_by_showcases = Column(Text, nullable=True)
    universal_name = Column(String(255), nullable=True)
    founded_on = Column(Date, nullable=True)
    similar_organizations = Column(Text, nullable=True)
    headquarters = Column(Text, nullable=True)

    def __repr__(self):
        return f"<EnrichedCompany(company_id={self.company_id}, company_name='{self.company_name}')>"

def get_engine():
    """Create and return a new SQLAlchemy engine."""
    engine_url = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    return create_engine(engine_url)

def get_session(engine):
    """Create and return a new SQLAlchemy session."""
    Session = sessionmaker(bind=engine)
    return Session()

def create_tables(engine):
    """Create all tables in the database."""
    Base.metadata.create_all(engine)
