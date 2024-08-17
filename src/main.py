from db.operations import add_company, get_company_by_id, get_enriched_company_by_id
from api.enrich import enrich_company_data


def add_company_endpoint():
    linkedin_url = input("Enter the company's LinkedIn URL: ")
    company_id = add_company(linkedin_url)
    if company_id:
        print(f"Company added successfully with ID: {company_id}")
    else:
        print("Failed to add company")

def get_company_endpoint():
    company_id = int(input("Enter the company ID: "))
    company = get_company_by_id(company_id)
    if company:
        print(f"Company found: {company}")
    else:
        print("Company not found")

def enrich_company_endpoint():
    company_id = int(input("Enter the company ID to enrich: "))
    company = get_company_by_id(company_id)
    if company:
        enriched_company = enrich_company_data(company.company_id, company.company_linkedin_url)
        if enriched_company:
            print(f"Company data enriched successfully: {enriched_company}")
        else:
            print("Failed to enrich company data")
    else:
        print("Company not found")

def display_enriched_data_endpoint():
    company_id = int(input("Enter the company ID to display enriched data: "))
    enriched_company = get_enriched_company_by_id(company_id)
    if enriched_company:
        print(f"Enriched company data: {enriched_company}")
    else:
        print("Enriched company data not found")

def main():
    while True:
        print("\n1. Add company")
        print("2. Get company")
        print("3. Enrich company data")
        print("4. Display enriched company data")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_company_endpoint()
        elif choice == '2':
            get_company_endpoint()
        elif choice == '3':
            enrich_company_endpoint()
        elif choice == '4':
            display_enriched_data_endpoint()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()