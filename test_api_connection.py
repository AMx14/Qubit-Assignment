import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def fetch_company_data_from_api(linkedin_url):
    api_url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/person_data_with_educations"
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY')
    }
    payload = {"link": linkedin_url}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()  # Assuming the response is in JSON format
            except ValueError:
                print("Response is not in JSON format.")
                return None
        else:
            print(f"API connection failed with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    linkedin_company_url = "http://www.linkedin.com/company/aep-energy"
    company_data = fetch_company_data_from_api(linkedin_company_url)
    if company_data:
        print(company_data)  # This will print out the enriched company data
