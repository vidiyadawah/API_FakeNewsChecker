# API_FakeNewsChecker

## Description
This Fake News Checker uses NewsAPI and python to create a program that will let users predict based on a Naives Bayes Classifier model, if the article they are reading is real news are fake news. The purpose of this program is to curb the spread of misinformation and help people know if what they are reading is accurate or not.

This program classifies news articles as either "Fake" or "Real" using the Naive Bayes Classifier. You can search the articles by title or by url. After you have found the article you can create a visualization, a sentimental analysis of the article or a word cloud of the article. You can also see a word cloud based off of the fake.csv and true.csv datasets.

## Installation
Check out the requirements.txt file to see what libraries you need to run the program.
pip install -r requirements.txt

Clone the repository using the following command line in git bash
git clone git@github.com:your_username/API_FakeNewsChecker.git

Create a config.py to store your API key and url, this will be imported into the program.
key = "your_unique_api_key"
url = "api_url"

Make sure you have the fake.csv and the true.csv. They can be found on kaggle https://www.kaggle.com/datasets/jainpooja/fake-news-detection or you could use different datasets with a similar structure.

##How To Run the Program
In your terminal run:
python main.py
And follow the prompts in your terminal

## Resources
Datasets: Fake News Dataset https://www.kaggle.com/datasets/jainpooja/fake-news-detection 
API: NewsAPI https://newsapi.org/ 
Visualizations: Inspired by WordCloud Library and TextBlob

## Demo
Here is a link to a video where I demo the project 