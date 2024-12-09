import requests
import matplotlib.pyplot as plt
import seaborn as sns

class NewsAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_articles(self, query, language='en', page_size=5): #uses NewsAPI, the works
        params = {
            'q': query,
            'language': language,
            'pageSize': page_size,
            'apiKey': self.api_key
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get('articles', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching articles: {e}")
            return []

class FactCheckAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def verify_claim(self, title): #verifying claims using google API
        params = {
            'query': title,
            'key': self.api_key
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get('claims', [])
        except requests.exceptions.RequestException as e:
            print(f"Error we cannot verify the claim: {e}")
            return []

class FakeNewsChecker:
    def __init__(self, news_api, fact_check_api): #this doesn't work idk whyyyyy
        self.news_api = news_api
        self.fact_check_api = fact_check_api

    def analyze_article(self, title):
        articles = self.news_api.fetch_articles(title)
        results = []

        for article in articles:
            fact_checks = self.fact_check_api.verify_claim(article['title'])
            results.append({
                'title': article['title'],
                'source': article['source']['name'],
                'fact_checks': fact_checks
            })

        return results
    
    def filter_relevant_articles(articles, query):#gets the related articles based on th eusers search
        query_words = set(query.lower().split())
        ranked_articles = sorted(
            articles,
            key=lambda article: len(query_words & set(article['title'].lower().split())),
            reverse=True
        )
        return ranked_articles
