from news_api import News_API
from config import key, api_url
from predict_news import NaiveBayesClassifier
import pandas as pd

def main():
    #Test that the API works, Can get the article from the title
    #Need to add more error handling and second option
    #Ex Title: Inside Elon Musk’s messy breakup with OpenAI, Mortgage Predictions: Uncertainty over Trump Sent Rates Higher. Here's What's Next
    api_key = key
    api_URL = api_url

    classifier = NaiveBayesClassifier()
    news_api = News_API(api_key, api_URL, classifier)

    news_api.train_the_classifier()

    # fake_data = pd.read_csv('fake.csv')   # You may want to try Git Large File Storage - https://git-lfs.github.com.
    # true_data = pd.read_csv('true.csv') #both files are over 50MB fix this later

    # fake_data['label'] = 'Fake'
    # true_data['label'] = 'Real'

    # combined_data = pd.concat([fake_data, true_data], ignore_index=True)
    # classifer.train_the_model(combined_data)

    print("Hello welcome to Fake News Checker!\n This program is designed to let you the user, check to see if the article you are reading has correct information or if it has fake information.\n Please proceed to get started\n")

    choice = '0'

    while choice != '3':
        choice = input("Press 1 to search by title. \nPress 2 to search by url. \nPress 3 to quit.\n")
        if choice == '1':
            print("Searching by title...")
            title = input("Type in the title of a news article.")
            prediction = news_api.article_by_title(title, title)
            if prediction:
                print(f"{title} is {prediction}.")
            else:
                print("Could not find an article with that title. Try double checking the correct title. Or search using a keyword or phrase instead. If it still doesn't work try searching by url instead.")
        elif choice == '2':
            url = input("Please enter the URL of the article you would like to check.")
            news_api.article_by_URL(url)

        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
        else:
            print("Please enter a choice.")
            

            
            

if __name__ == "__main__":
    main()