import requests
from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from ..models.search_history import SearchHistory

API_DICTIONARY = "https://api.dictionaryapi.dev/api/v2/entries/en/"


class WordSearch(View):
    def get(self, request: Request) -> Response:
        """
        Function returning word of the day or the searched word verified by api
        :param request: Request
        :return: Response with data: dict and status: status
        Response(
            {
                "word_search": "word" if word exists else "Not found"
            },
            status_code: int = 200 if word exists else 400
        )
        """
        word_searched = request.query_params.get("search", None)
        user = request.query_params.get("user", None)

        if word_searched is not None:
            response = requests.get(API_DICTIONARY + word_searched).json()
            if len(response) == 3:
                return Response({"word_searched": response["title"]}, status=status.HTTP_404_NOT_FOUND)
            SearchHistory.objects.create(user=user, search_query=word_searched)
        else:
            word_searched = self.get_word_of_the_day()

        return Response({"word_searched": word_searched}, status=status.HTTP_200_OK)

    @staticmethod
    def get_word_of_the_day() -> str:
        """
        Fetches from database the most searched word from a week ago and returns it
        :return: str
        """
        return SearchHistory.objects.latest('search_query').search_query
