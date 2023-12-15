
from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from decouple import config


class InstagramReelsFeed(APIView):
    RAPIDAPI_KEY = config('RAPIDAPI_KEY')  # Read from environment
    RAPIDAPI_HOST = config('RAPIDAPI_HOST')

    def get(self, request: Request) -> Response:
        user_posts = self.get_user_posts()

        hashtags = self.extract_hashtags(user_posts)

        top_posts = self.get_top_posts_from_rapidapi(hashtags)

        response_data = {
            'top_posts': [
                {
                    'post_id': post.get('id'),
                    'caption': post.get('caption', ''),
                    'image_url': post.get('image_url', ''),
                }
                for post in top_posts
            ]
        }

        return Response(data=response_data, status=status.HTTP_200_OK)


    def get_user_posts(self):

        url = f"https://{self.RAPIDAPI_HOST}/hashtag/feed/reels"
        querystring = {"hashtag": "summer"}  # Replace with your desired hashtag
        headers = {
            "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            "X-RapidAPI-Host": self.RAPIDAPI_HOST
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            user_posts = response.json()

            return user_posts

        except requests.RequestException as e:
            # Handle request errors
            print(f"Error fetching user posts from RapidAPI Instagram Reels feed: {e}")
            return []

    def extract_hashtags(self, posts):
        # Extract hashtags from posts
        hashtags = set()
        for post in posts:
            if isinstance(post, dict):  # Check if post is a dictionary
                hashtags.update(tag.strip('#') for tag in post.get('caption', '').split() if tag.startswith('#'))
        return hashtags

    def get_top_posts_from_rapidapi(self, hashtags):
        # Use RapidAPI Instagram Reels feed API to get top posts based on hashtags
        url = f"https://{self.RAPIDAPI_HOST}/hashtag/feed/reels"

        # Check if the hashtags set is empty
        if not hashtags:
            print("No hashtags available.")
            return []

        querystring = {"hashtag": hashtags.pop()}  # Assuming you want to use the first hashtag as the search term
        headers = {
            "X-RapidAPI-Key": self.RAPIDAPI_KEY,
            "X-RapidAPI-Host": self.RAPIDAPI_HOST
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            top_posts = response.json()

            return top_posts

        except requests.RequestException as e:
            # Handle request errors
            print(f"Error fetching top posts from RapidAPI Instagram Reels feed: {e}")
            return []
