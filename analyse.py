import os
from xml.dom.xmlbuilder import DocumentLS
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


#loading API keys
load_dotenv()
key = os.getenv('key')
endpoint = os.getenv('endpoint')

#authorizing the client
ta_credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint = endpoint, credential = ta_credential)

def sentiment_analysis(document):
    '''
    Function to analyze the scraped reviews

    Argument:
    Array of reviews

    Returns:
    Sentiment analysis
    '''

    #analyzing the sentiment
    response = client.analyze_sentiment(documents = document)[0]

    sentiment = response.sentiment
    positive_score = response.confidence_scores.positive
    negative_score = response.confidence_scores.negative
    neutral_score = response.confidence_scores.neutral

    overall_sentiment = {
        'sentiment' : response.sentiment,
        'positive_score' : response.confidence_scores.positive,
        'negative_score' : response.confidence_scores.negative,
        'neutral_score' : response.confidence_scores.neutral
    }

    return overall_sentiment

def opinion_mine(document):
    '''
    Function to get opinion of target words in reviews document

    Argument:
    An Array of reviews

    Returns:
    A dictionary with key as a target word and its value as the opinion of the target word
    '''
    
    opinions = {}

    for doc in document:
        arr = [doc]
        result = client.analyze_sentiment(arr, show_opinion_mining = True)
        doc_result = [k for k in result if not k.is_error]
        for d in doc_result:
            for s in d.sentences:
                for opinion in s.mined_opinions:
                    target = opinion.target
                    target_text = target.text
                    target_sentiment = target.sentiment
                    if target_text not in opinions:
                        opinions[target_text] = target_sentiment

    return opinions    


print(opinion_mine(document))