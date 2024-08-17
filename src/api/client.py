import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LinkedInDataFetcher:
    def __init__(self):
        self.api_url = "https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper/playground/apiendpoint_1ec7c221-8b53-41f6-8845-2dcdbd69ed6e"
        self.headers = {
            "X-RapidAPI-Host": "linkedin-bulk-data-scraper.p.rapidapi.com",
            "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY')
        }

    def fetch_enriched_data(self, linkedin_url):
        """
        Fetch enriched data for a company from the LinkedIn Bulk Data Scraper API.
        Args:
            linkedin_url (str): LinkedIn URL of the company to fetch data for.

        Returns:
            dict: A dictionary containing the enriched data or None if the request fails.
        """
        response = requests.post(self.api_url, json={"urls": [linkedin_url]}, headers=self.headers)

        # Debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # Check if the response content is not empty and status is OK
        if response.status_code == 200 and response.text:
            try:
                return response.json()
            except ValueError as e:
                print(f"JSON Decode Error: {e}")
                return None
        else:
            print("Failed to get a valid response")
            return None


# Example usage:
if __name__ == "__main__":
    fetcher = LinkedInDataFetcher()
    linkedin_url = "https://www.linkedin.com/company/example"

    enriched_data = fetcher.fetch_enriched_data(linkedin_url=linkedin_url)

    if enriched_data:
        print(enriched_data)
    else:
        print("Failed to fetch enriched data.")
