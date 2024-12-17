import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class NaiveBayesClassifier: #creates the model to predict the autehnticity of the article
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()

    def train_the_model(self, data):
        data = data.dropna(subset=['text', 'label'])
        X = data['text']
        y = data['label']
        X_vec = self.vectorizer.fit_transform(X)
        self.classifier.fit(X_vec, y)

    def predict(self, text):
        article_vec = self.vectorizer.transform([text])
        prediction = self.classifier.predict(article_vec)
        return prediction[0]






