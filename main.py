from config import NEWS_API_KEY, key, NEWS_API_URL, FACT_CHECK_URL
from NewsApi import NewsAPI, FactCheckAPI, FakeNewsChecker
from visuals import Visualize

def main():
    #get the apis from the config file
    news_api = NewsAPI(NEWS_API_KEY, NEWS_API_URL)
    fact_check_api = FactCheckAPI(key, FACT_CHECK_URL)
    checker = FakeNewsChecker(news_api, fact_check_api)

    #asks th euser to input the name of the article or a claim
    article_title = input("Enter the title of the news article or a claim you want to fact check: ")
    print("\nFetching news articles and checking for fact-checks...\n")
    results = checker.analyze_article(article_title) #checks the article and stores it in results variable

    if results:
        print("Analysis Results:")
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Source: {result['source']}")
            if result['fact_checks']:
                for check in result['fact_checks']:
                    print(f"Fact-Check: {check.get('textualRating', 'No rating')}")
            else:
                print("We could not fine any fact-check information.\n")


        Visualize.plot_sources(results) #plots the sources and the fact check stuff
        Visualize.plot_fact_checks(results)
    else:
        print("No articles found or an error occurred.")

if __name__ == "__main__": #runs the program the newsAPI works but the googleAPI doesn't work right now
    main()
#Test: Mpox is a reaction to COVID-19 vaccines