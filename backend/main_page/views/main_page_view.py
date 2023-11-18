from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main_page.views.word_search_view import WordSearch
from main_page.views.instagram_search_view import InstagramSearch


class MainPageView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        word_searched: Response = WordSearch.as_view()(request)
        instagram_search: Response = InstagramSearch.as_view()(request)

        if word_searched.status_code == 404:
            return word_searched

        aggregated_data = {
            **word_searched.data,
            **instagram_search.data
        }

        return Response(aggregated_data, status=status.HTTP_200_OK)
