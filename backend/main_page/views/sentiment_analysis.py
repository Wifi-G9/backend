import requests
from rest_framework.views import APIView

from django.urls import reverse

class SentimentAnalysis(APIView):
    @staticmethod
    def get_sentiment(text):
        """
        Calls the Sentiment Analysis API and returns the sentiment analysis result.
        :param text: str
        :return: Tuple[str, int]
        """
        # Use reverse to get the full URL with scheme and domain
        api_sentiment_analysis_url = reverse('sentiment_analysis')
        payload = {'text': text}
        response = requests.get(api_sentiment_analysis_url, params=payload)

        if response.status_code == 200:
            sentiment_result = response.json().get('sentiment', None)
            return sentiment_result, 200
        else:
            return None, response.status_code

    def process_sentiment_analysis(self, text):
        sentiment_analysis, status_code = self.get_sentiment(text)

        if status_code == 200:
            return sentiment_analysis
        else:
            return f"Error in sentiment analysis API (Status Code: {status_code})"
