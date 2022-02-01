import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def review_analysis(document):
    '''
    Function to analyze the scraped reviews

    Argument:
    Array of reviews

    Returns:
    Sentiment analysis, opinion mining
    '''
    #loading API keys
    load_dotenv()
    key = os.getenv('key')
    endpoint = os.getenv('endpoint')

    #authorizing the client
    ta_credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint = endpoint, credential = ta_credential)
    
    #analyzing the sentiment
    response = client.analyze_sentiment(documents = document)[0]
    print("Sentiment :", response.sentiment)
    print("overall scores: positive :", response.confidence_scores.positive, "Negative :", response.confidence_scores.negative)
