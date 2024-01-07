import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

API_FEED_URL = "https://instagram-statistics-api.p.rapidapi.com/posts"
API_INFO_URL = "https://instagram210.p.rapidapi.com/ig_profile"
RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
RAPIDAPI_HOST_FEED = os.environ.get('RAPIDAPI_HOST_FEED')
RAPIDAPI_HOST_INFO = os.environ.get('RAPIDAPI_HOST_INFO')


class UserFeedView(APIView):
    def get(self, request: Request, username=None):
        """
        Case of a good request
        Response(
            {
                "user_is_private": boolean,
                "user_profile_pic": "https://instagram...",
                "user_is_verified": boolean,
                "user_followers": number(int/long),
                "user_following": number(int/long),
                "user_biography": "str",
                "posts_month": [
                    {
                        "date": number(int/long),
                        "likes": number(int/long),
                        "comments": number(int/long),
                    },
                    {
                        "date": number(int/long),
                        "likes": number(int/long),
                        "comments": number(int/long),
                    },
                    ...
                ],
                "posts_year": [
                    {
                        "date": number(int/long),
                        "likes": number(int/long),
                        "comments": number(int/long),
                    },
                    {
                        "date": number(int/long),
                        "likes": number(int/long),
                        "comments": number(int/long),
                    },
                    ...
                ],
               "top_3_posts": [
                    {
                        "post_url": "https://www.instagram.com/p/...",
                        "post_type": "photo",  (string with specific value)
                        "post_text": "The Hollywood Reporter",   (string with the post text)
                        "post_hash_tags": list of str,
                        "post_mentions": list of str,
                        "posts_grade": "b" (string with specific value grade)
                        "post_image": "link to post image"
                    },
                    ...
                ]
            },
            status=status.HTTP_200_OK)
        """

        response_view = {}
        insta = self.request.query_params.get("insta", None)
        if insta is None:
            return Response("No username provided", status=status.HTTP_400_BAD_REQUEST)

        # First API Call (INFO)
        response = self.api_call_info(response_view, insta)
        if len(response_view) == 0:
            return Response("Username was not found", status=status.HTTP_404_NOT_FOUND)
        insta_fbid = response["fbid"]

        # Second API Call (FEED)
        response = self.api_call_feed(insta_fbid)
        self.__filter_data(response_view, response["data"]["posts"])

        return Response(response_view, status=status.HTTP_200_OK)

    @staticmethod
    def api_call_info(result_data, insta: str):
        params = {"ig": insta}
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST_INFO
        }
        response = requests.get(API_INFO_URL, headers=headers, params=params).json()
        if isinstance(response, list):
            response = response[0]
        else:
            return response
        result_data["user_is_private"] = response["is_private"]
        if not result_data["user_is_private"]:
            result_data["user_profile_pic"] = response["profile_pic_url_hd"]
            result_data["user_is_verified"] = response["is_verified"]
            result_data["user_followers"] = response["follower_count"]
            result_data["user_following"] = response["following_count"]
            result_data["user_biography"] = response["biography"]
        return response

    @staticmethod
    def api_call_feed(insta_fbid: str):
        current_date = datetime.now().date()
        params = {
            "cid": f"INST:{insta_fbid}",
            "from": (current_date - relativedelta(years=1)).strftime("%d.%m.%Y"),
            "to": current_date.strftime("%d.%m.%Y"),
            "sort": "date"
        }
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST_FEED
        }
        return requests.get(API_FEED_URL, headers=headers, params=params).json()

    @staticmethod
    def __filter_data(result_data, filter_data):
        current_date = datetime.now().date()
        one_month_ago = current_date - relativedelta(months=1)
        for entry in filter_data:
            entry['date'] = datetime.fromisoformat(entry['date'].rstrip("Z")).date()
        result_data["posts_month"] = []
        result_data["posts_year"] = []
        most_popular_posts = [None] * 3  # top 3 posts in ascending order
        most_engaged_posts = [0] * 3  # the engagement on the top 3 posts in ascending order
        smallest_engaged_post_idx = 0

        # TODO: make sure that the dates represent a full month or a full year
        for entry in filter_data:
            engagement_rate = [entry["likes"], entry["comments"]]

            if one_month_ago <= entry['date'] <= current_date:
                result_data["posts_month"].append({
                    'date': entry['date'],
                    'likes': engagement_rate[0],
                    'comments': engagement_rate[1]
                })

            result_data["posts_year"].append({
                'date': entry['date'],
                'likes': engagement_rate[0],
                'comments': engagement_rate[1]
            })

            engagement_sum = sum(engagement_rate)
            if most_engaged_posts[smallest_engaged_post_idx] < engagement_sum and entry["type"] == "photo":
                most_popular_posts[smallest_engaged_post_idx] = entry
                most_engaged_posts[smallest_engaged_post_idx] = engagement_sum
                # reset smallesr engaged post index
                for i in range(3):
                    if most_engaged_posts[i] < most_engaged_posts[smallest_engaged_post_idx]:
                        smallest_engaged_post_idx = i

        result_data["top_3_posts"] = []
        for i in range(3):
            most_popular_post = most_popular_posts[i]
            current_post = {}
            if most_popular_post is not None:
                current_post["post_image"] = most_popular_post["postImage"]
                current_post["post_url"] = most_popular_post["postUrl"]
                current_post["post_type"] = most_popular_post["type"]
                current_post["post_text"] = most_popular_post["text"]
                current_post["post_hash_tags"] = most_popular_post["hashTags"]
                current_post["post_mentions"] = []
                for mention in most_popular_post["mentions"]:
                    current_post["post_mentions"].append(mention["name"])
                current_post["post_grade"] = most_popular_post["mainGrade"]
            result_data["top_3_posts"].append(current_post)

