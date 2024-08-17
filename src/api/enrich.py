from .client import LinkedInDataFetcher
from ..db.operations import update_enriched_company

def enrich_company_data(company_id, linkedin_url):
    fetcher = LinkedInDataFetcher()
    enriched_data = fetcher.fetch_enriched_data(linkedin_url)

    if enriched_data:
        # Filter out unwanted fields
        filtered_data = {k: v for k, v in enriched_data.items() if not any(
            substring in k for substring in ['affiliatedOrganizations', 'locations', 'similarOrganizations'])}

        # Update the enriched company data in the database
        updated_company = update_enriched_company(company_id, filtered_data)
        return updated_company
    else:
        print(f"Failed to enrich data for company ID: {company_id}")
        return None