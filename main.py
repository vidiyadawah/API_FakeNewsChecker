from news_api import News_API
from config import key, api_url
from predict_news import NaiveBayesClassifier
from visual import FakeNewsCloud, TrueNewsCloud, FakeNewsSentiment, TrueNewsSentiment


def main():
    #Ex Title: Inside Elon Musk’s messy breakup with OpenAI, Mortgage Predictions: Uncertainty over Trump Sent Rates Higher. Here's What's Next
    api_key = key
    api_URL = api_url

    classifier = NaiveBayesClassifier()
    news_api = News_API(api_key, api_URL, classifier)

    news_api.train_the_classifier("fake.csv", "true.csv")

    print("Hello welcome to Fake News Checker!\nThis program is designed to let you the user, check to see if the article you are reading has correct information or if it has fake information.\n Please proceed to get started\n")

    choice = '0'
    option = '0'

    while choice != '5':
        choice = input("Press 1 to search by title. \nPress 2 to search by url. \nPress 3 to see a word cloud of fake news. \nPress 4 to see a world cloud of real news. \nPress 5 to quit.\n")
        if choice == '1':
            print("You have selected searching by title...")
            title = input("Type in the title of a news article.\n")
            prediction = news_api.article_by_title(title, title)
            if prediction:
                print(f"{title} is {prediction} news.")
                article_text = news_api.scrape_article(news_api.get_news(title), title)
            else:
                print("Could not find an article with that title. Try double checking the correct title. If it still doesn't work try searching by url instead.")
            print("\n Would you like to see a visual of the data? Press 1 for yes and 2 for no.")
            option = input("\nPress 1 or 2.")
            if option == '1':
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
            else:
                print("Alirght.")
        elif choice == '2':
            url = input("Please enter the URL of the article you would like to check.")
            news_api.article_by_URL(url)
        elif choice =='3':
            print("\nThis word cloud will show the most common words seen in fake news. This should give you an idea about how you can spot fake news yourself.")
            fake_news_cloud = FakeNewsCloud("fake.csv", "true.csv")
            fake_news_cloud.gen_fake_cloud()
        elif choice == '4':
            print("\nThis word cloud will show the most common words seen in real news. This should help you understand the language real news tend to use.")
            true_news_cloud = TrueNewsCloud("fake.csv", "true.csv")
            true_news_cloud.gen_true_cloud()
        elif choice == '5':
            print("Thank you for using the program. Goodbye!")
        else:
            print("Please enter a choice.")
            

            
            

if __name__ == "__main__":
    main()