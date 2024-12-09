from config import NEWS_API_KEY, key, NEWS_API_URL, FACT_CHECK_URL
from NewsApi import NewsAPI, FactCheckAPI, FakeNewsChecker
from visuals import Visualize

def main():
    news_api = NewsAPI(NEWS_API_KEY, NEWS_API_URL) #gets the keys from the cnofig file
    fact_check_api = FactCheckAPI(key, FACT_CHECK_URL)
    checker = FakeNewsChecker(news_api, fact_check_api)

    #user is suppose to input the name of the article or a claim to fact check like the world is flat or smth
    article_title = input("Enter the title of the news article or a claim you want to fact check: ")
    print("\nFetching news articles and checking for fact-checks...\n")
    results = checker.analyze_article(article_title)  #Checks the article and stores it in results variable

    
    if results:
        print("Analysis Results:")
        for result in results:
            #checking the keys
            # print(f"Result keys: {result.keys()}")
            
            #for when there is missing data for the claim text
            claim_text = result.get('text', 'Sorry but there is nothing available.')
            print(f"Claim: {claim_text}")
            
            if 'fact_checks' in result and result['fact_checks']:
                for check in result['fact_checks']:
                    if 'claimReview' in check:
                        for review in check['claimReview']:
                            publisher = review.get('publisher', {}).get('name', 'Unknown Publisher')
                            title = review.get('title', 'No title')
                            url = review.get('url', 'No URL')
                            review_date = review.get('reviewDate', 'No review date')
                            textual_rating = review.get('textualRating', 'No rating')

                            print(f"Publisher: {publisher}")
                            print(f"Title: {title}")
                            print(f"Website: {url}")
                            print(f"Review Date: {review_date}")
                            print(f"Textual Rating: {textual_rating} \n")
            else:
                print("No fact checks were found for this query.\n")

        Visualize.plot_sources(results)  #Plots the sources and the fact-check stuff need to fix this ;-;
        Visualize.plot_fact_checks(results)
    else:
        print("No articles were found or an error occurred.")




if __name__ == "__main__": #runs the program the newsAPI works but the googleAPI doesn't work right now
    main()
#Test: Mpox is a reaction to COVID-19 vaccines (this one doesn;t work)  
#False Story Claims Indiana Lunch Lady Fatally Poisoned More Than 300 People