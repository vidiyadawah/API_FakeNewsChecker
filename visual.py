import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from news_api import ClassifierModel
from textblob import TextBlob

class WordCloudGenerator: #parent class creating a word cloud to show common words in true/fake articles
    def __init__(self, fake_csv, true_csv):
        self.classifier_model = ClassifierModel()
        self.classifier_model.train_the_classifier(fake_csv, true_csv) #training using the model
        self.combined_data = self.classifier_model.combined_data #storing the data
    
    def gen_wordcloud(self, dataset, title): #creates the word cloud, dropna gets rid of the empty values
        word_cloud = WordCloud(width = 500, height = 500, background_color="white").generate(" ".join(dataset.dropna()))
        plt.figure(figsize=(10,6))
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(title)
        plt.show()
        
class FakeNewsCloud(WordCloudGenerator): #child class uses the fake.csv
    def __init__(self, fake_csv, true_csv):
        super().__init__(fake_csv, true_csv)
    
    def gen_fake_cloud(self):
        fake_dataset = self.combined_data[self.combined_data['label'] == 'Fake']['text'] #filtering so we only use the fake news
        self.gen_wordcloud(fake_dataset, "WordCloud Showing Fake News")

class TrueNewsCloud(WordCloudGenerator): #child class useds the true.csv
    def __init__(self, fake_csv, true_csv):
        super().__init__(fake_csv, true_csv)
    
    def gen_true_cloud(self):
        true_dataset = self.combined_data[self.combined_data['label'] == 'Real']['text']#filtering so we only use true news
        self.gen_wordcloud(true_dataset, "WordCloud Showing Real News")
    
class ArticleWordCloud(WordCloudGenerator): #child class doesn't use datasets
    def __init__(self):
        pass

    def gen_article_cloud(self, article_text):
        if not article_text:
            print("There is no text available to make the Word Cloud.") #error handling
            return
        
        print("Generating Word Cloud for the article please give me a moment...")
        word_cloud = WordCloud(width=500, height=500, background_color="white").generate(article_text)
        plt.figure(figsize=(10, 6))
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("WordCloud of the Searched Article")
        plt.show()

class SentimentAnalysis: #parent class to do the sentiment analysis
    def __init__(self):
        pass

    def analyze_sentiment(self, text):
        sentences = text.split(".") #split the article seperated by a period
        pos_count = 0
        neg_count = 0
        neu_count = 0
        for sentence in sentences:
            blob = TextBlob(sentence)
            sentiment = blob.sentiment.polarity #the polarity decides if its negative, positive or neutral
            if sentiment > 0.1:
                pos_count += 1
            elif sentiment < -0.1:
                neg_count+= 1
            else:
                neu_count+= 1 
        total_sentences = pos_count + neg_count + neu_count
        if total_sentences ==0: #in case the total is somehow 0. so we don't divide by 0
            return None
        
        pos_percent = (pos_count/total_sentences)
        neg_percent = (neg_count/total_sentences)
        neu_percent = (neu_count/total_sentences)
        return pos_percent, neg_percent, neu_percent
    
    def plot_sentiment(self, pos_percent, neg_percent, neu_percent): #creates the visual with colors representing each category
        labels = ['Positive','Negative', "Neutral" ]
        sizes = [pos_percent, neg_percent, neu_percent]
        colors = ['lightgreen', 'lightcoral', 'lightgray']
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title("Sentiment Analysis of the Article")
        plt.show()


class FakeNewsSentiment(SentimentAnalysis):
    def __init__(self):
        super().__init__()
    
    def analyze_fake_sentiment(self, text):
        sentiment_percentages = self.analyze_sentiment(text) #parent function
        if sentiment_percentages:
            positive_percent, negative_percent, neutral_percent = sentiment_percentages
            print("Fake News Sentiment Analysis:")
            self.plot_sentiment(positive_percent, negative_percent, neutral_percent) #plots the analysis
        else:
            print("Could not analyze sorry.")

class TrueNewsSentiment(SentimentAnalysis):
    def __init__(self):
        super().__init__()
    
    def analyze_true_sentiment(self, text):
        sentiment_percentages = self.analyze_sentiment(text)
        if sentiment_percentages:
            positive_percent, negative_percent, neutral_percent = sentiment_percentages
            print("True News Sentiment Analysis:")
            self.plot_sentiment(positive_percent, negative_percent, neutral_percent)
        else:
            print("Could not analyze sorry.")



