from news_api import News_API
from config import key, api_url

def main():
    #Test that the API works, Can get the article from the title
    #Need to add more error handling and second option
    #Ex Title: Inside Elon Musk’s messy breakup with OpenAI
    news_api = News_API(api_key=key, api_url=api_url)
    choice = '0'

    while choice != '3':
        print(f"Current choice: {choice}")
        choice = input("Press 1 to search by title. \nPress 2 to search by url. \nPress 3 to quit.\n")
        if choice == '1':
            print("Searching by title...")
            query = input("Type in the title of a news article.")
            articles = news_api.get_news(query, page_size=1) #only gets one article
            if articles:
                article = articles[0]
                print(f"\nTitle: {article['title']}")

                full_article = news_api.scrape_article(articles, article['title'])
                if full_article:
                    print("\nFound the full article.\n")
                    print(full_article)

                else:
                    print("I was not able to get the article.")
            else:
                print("Could not find an article with that title.")
        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
        else:
            print("Please enter a choice.")
            

            
            

if __name__ == "__main__":
    main()