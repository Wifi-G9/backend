import os
import random

import requests
import json
import re
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from main_page.views.sentiment_analysis_view import SentimentAnalysis

API_HOST = "instagram-api-20231.p.rapidapi.com"
POSTS_NUMBER = 5
HASHTAG_PATTERN = r'#\w+\b'

workaround = ""


class InstagramSearch(APIView):
    def get(self, request: Request) -> Response:
        """
        Function to return top "POSTS_NUMBER" posts from instagram and the data related to them
        :param request: Request
        :return Response with data outlined in docs/endpoints/README.md, status code will be 404 if an error has
        occurred or 200 if the data was received and parsed correctly
        """
        # return Response(self.mock_data(), status=status.HTTP_200_OK)
        # if your .env file does not have this key, a mock data for debugging will be sent as the api has a limit on
        # the requests
        api_key = os.environ.get("RAPID_API_KEY")
        # if api_key is None:
        if api_key is None:
            return Response(self.mock_data(), status=status.HTTP_200_OK)

        # prepare the data for the request
        query = request.query_params.get("query")
        if query is None or query == "wordOfTheDay":
            return Response(self.mock_data(), status=status.HTTP_404_NOT_FOUND)

        # FIXME: this should not exist, the frontend has a bug and sends like 4 requests per click so if if the query
        # FIXME: sent is the same, do not process it. Hopefully we will remove this ASAP
        global workaround
        if workaround == query:
            return Response({"error": "too many requests"}, status=status.HTTP_404_NOT_FOUND)
        else:
            workaround = query

        url = f"https://instagram-api-20231.p.rapidapi.com/api/hashtag_media/{query}"
        querystring = {"feed_type": "top"}

        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": API_HOST
        }

        response = requests.get(url, headers=headers, params=querystring)

        try:
            # parse the request to extract the relevant data
            posts: json = response.json()["data"]["medias"][:POSTS_NUMBER]
            result_json = []

            for post in posts:
                # print(post)
                code: str = post["code"]
                description = post["caption"]["text"]
                hashtags_list: [str] = re.findall(HASHTAG_PATTERN, description)

                sentiment_analysis = SentimentAnalysis.fetch_analysis(description)
                print(sentiment_analysis)

                current_json = {
                    "link": f"https://www.instagram.com/p/{code}/",
                    "description": description,
                    "sentiment_analysis": {
                        "sentiment": sentiment_analysis["sentiment"],
                        "score": sentiment_analysis["score"]
                    },
                    "likes": post["like_count"],
                    "comments": post["comment_count"],
                    "hashtags": hashtags_list,
                    "engagement_score": random.uniform(0.0, 45.5),
                    "image_description": "N/A"
                }
                result_json.append(current_json)
        except KeyError:
            return Response({"error": "key error"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"posts-list": result_json}, status=status.HTTP_200_OK)

    @staticmethod
    def mock_data() -> dict:
        return {"posts-list": [
            {
                "link": "https://mock-link.com",
                "description": "Mock data",
                "sentiment_analysis": {
                    "sentiment": "positive",
                    "score": 0.9
                },
                "likes": 1000,
                "comments": 500,
                "hashtags": [
                    "#AI",
                    "#artificialintelligence",
                    "#future"
                ],
                "engagement_score": 1500,
                "image_description": "A person using a computer with a futuristic interface."
            },
            {
                "link": "https://www.instagram.com/p/C0HZCaoidDN/",
                "description": "AI is the future!",
                "sentiment_analysis": {
                    "sentiment": "positive",
                    "score": 0.9
                },
                "likes": 1000,
                "comments": 500,
                "hashtags": [
                    "#AI",
                    "#artificialintelligence",
                    "#future"
                ],
                "engagement_score": 1500,
                "image_description": "A person using a computer with a futuristic interface."
            },
            {
                "link": "https://www.instagram.com/p/CWQ3456j_rX/",
                "description": "AI is changing the world.",
                "sentiment_analysis": {
                    "sentiment": "positive",
                    "score": 0.8
                },
                "likes": 800,
                "comments": 400,
                "hashtags": [
                    "#AI",
                    "#artificialintelligence",
                    "#change"
                ],
                "engagement_score": 1200,
                "image_description": "A group of robots working together in a factory."
            },
            {
                "link": "https://www.instagram.com/p/CWO6789j_rX/",
                "description": "AI is amazing!",
                "sentiment_analysis": {
                    "sentiment": "positive",
                    "score": 1.0
                },
                "likes": 600,
                "comments": 300,
                "hashtags": [
                    "#AI",
                    "#artificialintelligence",
                    "#amazing"
                ],
                "engagement_score": 900,
                "image_description": "A child playing with an AI-powered robot."
            }
        ]}
