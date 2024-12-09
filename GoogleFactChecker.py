import requests
from config import FACT_CHECK_URL, key

class FactCheckAPI:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url

    def check_article(self, title, article_text):
        params = {'query': title, 'key': self.api_key}

        try:
            # print(f"API URL: {self.url}")
            # print(f"API Key: {self.api_key}")

            response = requests.get(self.url, params=params) #making the request

            #to debug bc i was having issues
            # print(f"API Status Code: {response.status_code}")
            # print(f"API Response: {response.text}")

            if response.status_code == 200: #checks if it contains the claims data
                data = response.json()
                claims_info = []

                if 'claims' in data: #claims has to be present 
                    for claim in data['claims']:
                        claim_data = {
                            'text': claim.get('text', 'No text found'),
                            'fact_checks': []
                        }
                        if 'claimReview' in claim:
                            for review in claim['claimReview']:
                                claim_data['fact_checks'].append({
                                    'publisher': review.get('publisher', {}).get('name', 'Unknown Publisher'),
                                    'title': review.get('title', 'No title'),
                                    'url': review.get('url', 'No URL'),
                                    'review_date': review.get('reviewDate', 'No review date'),
                                    'textual_rating': review.get('textualRating', 'No rating')
                                })
                        claims_info.append(claim_data) #adds the data

                if claims_info:
                    return claims_info
                else:
                    print("No claims found for this query.")
                    return []
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}") #error handling stuff
                return []

        except requests.exceptions.RequestException as e:
            print(f"Error searching fact-checks: {e}")
            return []
