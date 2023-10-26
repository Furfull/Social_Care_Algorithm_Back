from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from app.parameters import ENDPOINT, KEY

def sample_analyze_sentiment(document: str, endpoint = ENDPOINT, key = KEY) -> dict:

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    documents = [
        document
    ]

    result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        return({'text':documents[idx],
                'overview': doc.sentiment,
                'positive': str(doc.confidence_scores.positive),
                'neutral': str(doc.confidence_scores.neutral),
                'negative': str(doc.confidence_scores.negative)})

