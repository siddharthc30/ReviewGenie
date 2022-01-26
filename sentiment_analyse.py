import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()
key = os.getenv('key')
endpoint = os.getenv('endpoint')

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint = endpoint, credential = ta_credential)

    return text_analytics_client


client = authenticate_client()

def review_analysis(client, document):
    #document = ["A visit to Palace Heights for lunch or dinner always is very satisfying. This age old restaurant has been a favorite to many. I have been visiting now and then for last 20 years, the taste, the quality, the service remains the same. The ambience is always great and as this Bar and Restaurant is in the 8th floor, the view of the city is too good. the side walls majorly are glass windows. Every item in the menu is made with perfection. Weekends waiting time is huge. Little problem with the parking. Valet is available. One shud visit this place and feel it."]
    response = client.analyze_sentiment(documents = document)[0]
    print("Sentiment :", response.sentiment)
    print("overall scores: positive :", response.confidence_scores.positive, "Negative :", response.confidence_scores.negative)

review_analysis(client)