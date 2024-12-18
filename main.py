from news_api import News_API #to gather the data
from config import key, api_url #to get API credentials 
from predict_news import NaiveBayesClassifier #to use the predictive model
from visual import FakeNewsCloud, TrueNewsCloud, ArticleWordCloud, FakeNewsSentiment, TrueNewsSentiment #to create the visuals


def main():
    api_key = key #sets up the key and the url, this is imported from a config.py file
    api_URL = api_url

    classifier = NaiveBayesClassifier()
    news_api = News_API(api_key, api_URL, classifier)

    news_api.train_the_classifier("fake.csv", "true.csv") #trains the model

    print("Hello welcome to Fake News Checker!\nThis program is designed to let you the user, check to see if the article you are reading has correct information or if it has fake information.\nPlease proceed to get started.\n")

    choice = '0' #intializes the choice and option to 0 so the loop can run
    option = '0'

    while choice != '5': #doesn't end unless the user decides to quit by pressing 5
        choice = input("Press 1 to search by title. \nPress 2 to search by url. \nPress 3 to see a word cloud of fake news. \nPress 4 to see a word cloud of real news. \nPress 5 to quit.\n")
        if choice == '1':
            print("You have selected searching by title...")
            title = input("Type in the title of a news article.\n")
            prediction = news_api.article_by_title(title, title)
            if prediction:
                print(f"'{title}' is predicted to be {prediction} news.")
                article_text = news_api.scrape_article(news_api.get_news(title), title)
            else:
                print("Could not find an article with that title. Try double checking the correct title. If it still doesn't work try searching by url instead.") #if we can't find the article
            print("\nWould you like to see a Sentimental Analysis of the data? Or a Word Cloud of the article? Press 1 for a Sentimental Analysis, 2 for a Word Cloud, or 3 to exit.")
            option = input("\nPress 1, 2 or 3.")
            if option == '1': #creates a pie chart
                print("Loading the visualization please give me a moment...")
                if article_text:
                    if prediction == "Fake":
                        fake_sentiment = FakeNewsSentiment()
                        fake_sentiment.analyze_fake_sentiment(article_text)
                    else:
                        true_sentiment = TrueNewsSentiment()
                        true_sentiment.analyze_true_sentiment(article_text)
                else:
                    print("Could not load the visual sorry!")
            elif option == '2': #creates a word cloud
                if 'article_text' in locals() and article_text:
                    print("Loading the visualization please give me a moment...")
                    article_wordcloud = ArticleWordCloud()
                    article_wordcloud.gen_article_cloud(article_text)
                else:
                    print("Could not make the Word Cloud sorry!")
            else:
                print("Alright.")
        elif choice == '2':
            url = input("Please enter the URL of the article you would like to check.")
            news_api.article_by_URL(url)
        elif choice =='3': #word cloud based on the fake.csv dataset
            print("\nThis word cloud will show the most common words seen in fake news. This should give you an idea about how you can spot fake news yourself.")
            fake_news_cloud = FakeNewsCloud("fake.csv", "true.csv")
            fake_news_cloud.gen_fake_cloud()
        elif choice == '4': #word cloud based on the true.csv dataset
            print("\nThis word cloud will show the most common words seen in real news. This should help you understand the language real news tend to use.")
            true_news_cloud = TrueNewsCloud("fake.csv", "true.csv")
            true_news_cloud.gen_true_cloud()
        elif choice == '5': #ends the loop and the program
            print("Thank you for using the program. Goodbye!")
        else:
            print("Please enter a choice.")
        

if __name__ == "__main__":  #runs the program
    main()