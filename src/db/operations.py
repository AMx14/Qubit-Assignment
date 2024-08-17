from sqlalchemy.exc import SQLAlchemyError
from db.models import Company, EnrichedCompany, get_engine, get_session

# Create engine and session
engine = get_engine()
session = get_session(engine)

def add_company(linkedin_url):
    """Add a new company to the companies table."""
    try:
        new_company = Company(company_linkedin_url=linkedin_url)
        session.add(new_company)
        session.commit()
        print(f"Company added with LinkedIn URL: {linkedin_url}")
        return new_company.company_id
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding company: {e}")
        return None

def get_company_by_id(company_id):
    """Retrieve a company from the companies table by its ID."""
    try:
        company = session.query(Company).filter_by(company_id=company_id).first()
        return company
    except SQLAlchemyError as e:
        print(f"Error retrieving company: {e}")
        return None

def add_enriched_company(data):
    """Add an enriched company to the enriched_companies table."""
    try:
        enriched_company = EnrichedCompany(**data)
        session.add(enriched_company)
        session.commit()
        print(f"Enriched company added with ID: {enriched_company.company_id}")
        return enriched_company
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding enriched company: {e}")
        return None

def update_enriched_company(company_id, update_data):
    """Update an existing enriched company."""
    try:
        enriched_company = session.query(EnrichedCompany).filter_by(company_id=company_id).first()
        if enriched_company:
            for key, value in update_data.items():
                setattr(enriched_company, key, value)
            session.commit()
            print(f"Enriched company with ID {company_id} updated.")
            return enriched_company
        else:
            print(f"Enriched company with ID {company_id} not found.")
            return None
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating enriched company: {e}")
        return None

def get_enriched_company_by_id(company_id):
    """Retrieve an enriched company from the enriched_companies table by its ID."""
    try:
        enriched_company = session.query(EnrichedCompany).filter_by(company_id=company_id).first()
        return enriched_company
    except SQLAlchemyError as e:
        print(f"Error retrieving enriched company: {e}")
        return None
