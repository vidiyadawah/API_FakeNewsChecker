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
    
# fake_data = pd.read_csv('fake.csv')   # You may want to try Git Large File Storage - https://git-lfs.github.com.
# true_data = pd.read_csv('true.csv') #both files are over 50MB fix this later

# fake_data['label'] = 'Fake'
# true_data['label'] = 'Real'

# combined_data = pd.concat([fake_data, true_data], ignore_index=True)

# nb_classifier = NaiveBayesClassifier()
# nb_classifier.train_the_model(combined_data)





