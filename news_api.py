from config import key, api_url #gets the key WITHOUT showing it to everyone in the world
import requests
from newspaper import Article
import pandas as pd
from predict_news import NaiveBayesClassifier

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
    def __init__(self, api_key, api_url, classifier=None):
        super().__init__(api_key, api_url)        
        if classifier is None:
            self.classifier = NaiveBayesClassifier()
        else:
            self.classifier = classifier

    def get_news(self, query, language ="en", page_size=1): #the language of the article is in english and page size is how many articles are retrieved
        params = {"q" : query, "language" : language, "pageSize" : page_size, "APIkey" : self.API_key}
        response_data = self.make_request(params)
        if response_data:
            #print(f"API Respnse: {response_data}") #check if the Api is working
            return response_data.get("articles", [])
        else:
            print(f"There was an error with the API and we couldn't find your article: {response_data.status_code}, {response_data.json()}") #error handling if the article can't be found
            return []
        

    def train_the_classifier(self):
        fake_data = pd.read_csv('fake.csv')   # You may want to try Git Large File Storage - https://git-lfs.github.com.
        true_data = pd.read_csv('true.csv') #both files are over 50MB fix this later

        fake_data['label'] = 'Fake' #adds another column with fake for the the fake data and real for the true data
        true_data['label'] = 'Real'

        combined_data = pd.concat([fake_data, true_data], ignore_index=True)
        self.classifier.train_the_model(combined_data)


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
            
        for article in articles:
            if title.strip().lower() in article['title'].strip().lower(): #finds a title similar if there's an issue finding the exact title
                article_url = article['url']
                scraped_article = Article(article_url)
                scraped_article.download() 
                scraped_article.parse()
                return scraped_article.text

    def article_by_title(self, query, title): #gets the article from the user inputting a title
        articles = self.get_news(query, page_size=1) #only gets one article
        if articles:
            full_article = self.scrape_article(articles, title)
            if full_article:
                 print("Found the full article.\n")
                 prediction = self.classifier.predict(full_article)
                 print(f"The article {title} is {prediction} news.")
                 return prediction
        else:
            print("Can't check the article please double check the title.")
            return None


    def article_by_URL(self, url): #same as the previous function just using the url instead of the title
        try:
            scraped_article = Article(url)
            scraped_article.download()
            scraped_article.parse()
            full_article = scraped_article.text
            if full_article:
                print("Found the full article.\n")
                prediction = self.classifier.predict(full_article)
                print(f"The article found from the URL is {prediction} news.")
                return prediction
        except Exception as e:
            print(f"Could not get the article because of an error: {e}")
            return None



        



