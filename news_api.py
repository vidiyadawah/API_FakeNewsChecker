from config import key, api_url #gets the key WITHOUT showing it to everyone in the world
import requests
from newspaper import Article

class News_API:
    def __init__(self):
        self.API_key = key
        self.API_url = api_url

    def get_news(self, query, language ="en", page_size=1): #the language of the article is in english and page size is how many articles are retrieved
        params = {"q" : query, "language" : language, "pageSize" : page_size, "APIkey" : self.API_key}
        response = requests.get(self.API_url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            print(f"There was an error with the API and we couldn't find your article: {response.status_code}, {response.json()}") #error handling if the article can't be found
        
    def scrape_article(self, articles, title): #gets the article from the title and scrapes the whole thing, don't do this with articles you have to pay for
        for article in articles:
            if article['title'].lower() == title.lower():
                article_url = article('url')
                scraped_article = Article(article_url)
                scraped_article.download() #downlads the html from the url of the article
                scraped_article.parse()
                return scraped_article.text
            else: 
                print(f"Can't find the article, so I can't complete this task.")



        



