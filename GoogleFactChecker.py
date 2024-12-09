import requests
from config import FACT_CHECK_URL, key

class FactCheckAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = FACT_CHECK_URL

    def check_article(self, title, article_text):
        params = {
            'query': title, 
            'key': self.api_key
        }

        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            data = response.json()

            if 'claims' in data:
                return data['claims']
            return []
        except requests.exceptions.RequestException as e:
            print(f"Error searching fact-checks: {e}")
            return []

    def optimize_query(title):
        keywords = title.split()  #splits the string
        important_keywords = [word for word in keywords if len(word) > 3]  #Removes the non keywords
        return " ".join(important_keywords[:5])  
