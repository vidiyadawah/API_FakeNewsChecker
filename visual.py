import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from news_api import ClassifierModel
from textblob import TextBlob

class WordCloudGenerator: #parent class creating a word cloud to show common words in true/fake articles
    def __init__(self, fake_csv, true_csv):
        self.classifier_model = ClassifierModel()
        self.classifier_model.train_the_classifier(fake_csv, true_csv)
        self.combined_data = self.classifier_model.combined_data
    
    def gen_wordcloud(self, dataset, title):
        word_cloud = WordCloud(width = 500, height = 500, background_color="white").generate(" ".join(dataset.dropna()))
        plt.figure(figsize=(10,6))
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(title)
        plt.show()
        
class FakeNewsCloud(WordCloudGenerator): #child class
    def __init__(self, fake_csv, true_csv):
        super().__init__(fake_csv, true_csv)
    
    def gen_fake_cloud(self):
        fake_dataset = self.combined_data[self.combined_data['label'] == 'Fake']['text']
        self.gen_wordcloud(fake_dataset, "WordCloud Showing Fake News")

class TrueNewsCloud(WordCloudGenerator): #child class
    def __init__(self, fake_csv, true_csv):
        super().__init__(fake_csv, true_csv)
    
    def gen_true_cloud(self):
        true_dataset = self.combined_data[self.combined_data['label'] == 'Real']['text']
        self.gen_wordcloud(true_dataset, "WordCloud Showing Real News")
    

class SentimentAnalysis: #parent class to do the sentiment analysis
    def __init__(self):
        pass

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity 
        if sentiment > 0.1: #categories are defined by a polarity score
            return 'Positive'
        elif sentiment < -0.1:
            return 'Negative'
        else:
            return "Neutral"
        
    def plot_sentiment(self, s_label): #using a pie chart
        labels = ['Positive','Negative', "Neutral" ]
        sizes= [0,0,0]

        if s_label == 'Positive':
            sizes[0]= 1
        elif s_label == 'Negative':
            sizes[1] = 1
        else:
            sizes[2] = 1

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral', 'lightgray'])
        plt.title(f"Sentiment Analysis of the Article: {s_label}")
        plt.show()

class FakeNewsSentiment(SentimentAnalysis):
    def __init__(self):
        super().__init__()
    
    def analyze_fake_sentiment(self, text):
        s_label = self.analyze_sentiment(text)
        self.plot_sentiment(s_label)

class TrueNewsSentiment(SentimentAnalysis):
    def __init__(self):
        super().__init__()
    
    def analyze_true_sentiment(self, text):
        s_label = self.analyze_sentiment(text)
        self.plot_sentiment(s_label)



