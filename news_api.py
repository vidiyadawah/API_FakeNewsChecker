from config import key, api_url #gets the key WITHOUT showing it to everyone in the world
import requests
from newspaper import Article

class API: #parent class
    def __init__(self, api_key, api_url):
        self.API_key = api_key
        self.API_url = api_url

    def make_request(self, params):
        response = requests.get(self.API_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong with the API: {response.status_code}, {response.json()}")
            return None



class News_API(API): #child class inheriting the parent class
    def __init__(self, api_key, api_url):
        super().__init__(api_key, api_url)        

    def get_news(self, query, language ="en", page_size=1): #the language of the article is in english and page size is how many articles are retrieved
        params = {"q" : query, "language" : language, "pageSize" : page_size, "APIkey" : self.API_key}
        response_data = self.make_request(params)
        if response_data:
            print(f"API Respnse: {response_data}") #check if the Api is working
            return response_data.get("articles", [])
        else:
            print(f"There was an error with the API and we couldn't find your article: {response_data.status_code}, {response_data.json()}") #error handling if the article can't be found
            return []

    def scrape_article(self, articles, title): #gets the article from the title and scrapes the whole thing, don't do this with articles you have to pay for
        for article in articles:
            if article['title'].lower() == title.lower():
                article_url = article['url']
                scraped_article = Article(article_url)
                scraped_article.download() #downlads the html from the url of the article
                scraped_article.parse()
                return scraped_article.text
            else: 
                print(f"Can't find the article, so I can't complete this task.")



        



