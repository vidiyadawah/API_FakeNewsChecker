import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class NaiveBayesClassifier: #creates the model to predict the autehnticity of the article
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()

    def train_the_model(self, data):
        data = data.dropna(subset=['text', 'label']) #cleans the data by dropping the rows that are empty
        X = data['text'] #uses the text and label column for X and y 
        y = data['label']
        X_vec = self.vectorizer.fit_transform(X) #Converts the text data into a TF-IDF matrix
        self.classifier.fit(X_vec, y) #does the training 

    def predict(self, text):
        article_vec = self.vectorizer.transform([text]) #converts text to vector
        prediction = self.classifier.predict(article_vec)
        return prediction[0]






