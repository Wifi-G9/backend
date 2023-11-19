import os
import requests
from rest_framework import status

from rest_framework.views import View
from rest_framework.request import Request
from rest_framework.response import Response

API_HOST = "text-analysis12.p.rapidapi.com"


class SentimentAnalysis(View):
    def get(self, request: Request) -> Response:
        """
        Calls the Sentiment Analysis API and returns the sentiment analysis result.
        :param request: request
        :return: Tuple[str, int]
        """

        api_key = os.environ.get("RAPID_API_KEY")
        if api_key is None:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        text = request.query_params.get("text")
        if text is None:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        url = "https://text-analysis12.p.rapidapi.com/sentiment-analysis/api/v1.1"
        payload = {
            "language": "english",
            "text": text
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": API_HOST
        }

        response = requests.post(url, json=payload, headers=headers)

        response_json = response.json()
        overall_sentiment = response_json["sentiment"]
        sentiment_score = response_json["aggregate_sentiment"]["compound"]
        result_json = {
            "sentiment": overall_sentiment,
            "score": sentiment_score
        }

        return Response(result_json, status=status.HTTP_200_OK)
