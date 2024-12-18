from config import key, api_url #gets the key WITHOUT showing it to everyone in the world
import requests
from newspaper import Article
import pandas as pd
from predict_news import NaiveBayesClassifier

class API: #parent class to handle the API behind the scenes logic 
    def __init__(self, api_key, api_url):
        self.API_key = api_key
        self.API_url = api_url

    def make_request(self, params):
        response = requests.get(self.API_url, params=params) #sends a get request to the API with the params
        if response.status_code == 200: #checks if the request went through
            return response.json()
        else: #error handling 
            print(f"Something went wrong with the API: {response.status_code}, {response.json()}")
            return None

class ClassifierModel: #another parent class
    def __init__(self, classifier=None):   
        if classifier is None: #defaults to the Niave Bayes model
            self.classifier = NaiveBayesClassifier()
        else:
            self.classifier = classifier
        self.combined_data = None #creating and storing the combined data

    def train_the_classifier(self, fake_csv, true_csv):
        fake_data = pd.read_csv(fake_csv)   
        true_data = pd.read_csv(true_csv) 
        fake_data['label'] = 'Fake' #adds another column with fake for the the fake data and real for the true data
        true_data['label'] = 'Real'

        self.combined_data = pd.concat([fake_data, true_data], ignore_index=True)
        self.classifier.train_the_model(self.combined_data) #training the model after combining the datasets
    
    def predict_article(self, text):
        return self.classifier.predict(text) #does the predict


class News_API(API, ClassifierModel): #child class inheriting the parent class
    def __init__(self, api_key, api_url, classifier=None):
        API.__init__(self, api_key, api_url)
        ClassifierModel.__init__(self, classifier)

    def get_news(self, query, language ="en", page_size=1): #the language of the article is in english and page size is how many articles are retrieved
        params = {"q" : query, "language" : language, "pageSize" : page_size, "APIkey" : self.API_key}
        response_data = self.make_request(params)
        if response_data:
            return response_data.get("articles", []) #if the page size is greater than 1 this would return a list of articles
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
                article_text = scraped_article.text #stores the article in a variable to be used later
                return article_text
            else: 
                print(f"Can't find the article, so I can't complete this task.")
            
        for article in articles:
            if title.strip().lower() in article['title'].strip().lower(): #finds a title similar if there's an issue finding the exact title
                article_url = article['url']
                scraped_article = Article(article_url)
                scraped_article.download() 
                scraped_article.parse()
                article_text = scraped_article.text
                return article_text

    def predict_from_text(self, text, source="N/A", author = "N/A", date_published="N/A", url="N/A"): #if we can't get this info it will default to N/a
        prediction = self.classifier.predict(text)
        print(f"Source: {source} \nAuthor: {author} \nDate Published: {date_published} \nURL: {url}")
        return prediction

    def article_by_title(self, query, title): #gets the article from the user inputting a title
        articles = self.get_news(query, page_size=3) #only gets a few article
        if articles:
            for article in articles: #looks for a match 
                if title.strip().lower() in article['title'].strip().lower():
                    full_article = self.scrape_article(articles, title)
            if full_article:
                 source =article.get('source', {}).get('name', 'N/A')
                 author =article.get('author', 'N/A')
                 date_published =article.get('publishedAt','N/A')
                 url = article.get('url', 'N/A')
                 return self.predict_from_text(full_article, source=source,date_published =date_published, author = author, url =url)
        else:
            print("Can't check the article please double check the title.")
            return None


    def article_by_URL(self, url): #same as the previous function just using the url instead of the title
        try:
            scraped_article = Article(url)
            scraped_article.download()
            scraped_article.parse()
            return self.predict_from_text(scraped_article.text, source="URL")
        except Exception as e:
            print(f"Could not get the article because of an error: {e}")
            return None



        



