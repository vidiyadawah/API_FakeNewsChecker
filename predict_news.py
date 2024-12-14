import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

#put the predicting stuff here
data = pd.read_csv('fake.csv')

# Separate the text and labels
X = data['text']
y = data['label']

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_vec, y)

# Make predictions on the new data set
new_data = ['This is a real news article.', 'This is a fake news article.']
new_vec = vectorizer.transform(new_data)
predictions = classifier.predict(new_vec)

# Print predictions
print(predictions)