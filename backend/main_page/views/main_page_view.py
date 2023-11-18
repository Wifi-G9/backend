from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main_page.views.word_search_view import WordSearch
from main_page.views.instagram_search_view import InstagramSearch
from main_page.views.chatgpt_description_view import ChatGPTDescription


class MainPageView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        word_searched: Response = WordSearch.as_view()(request)
        instagram_search: Response = InstagramSearch.as_view()(request)

        if word_searched.status_code == 404:
            return word_searched

        word_searched_data=word_searched.data["word_searched"]
        description: Response = ChatGPTDescription.as_view()(request,word_searched_data)

        if description.status_code != 200:
            return description

        aggregated_data = {
            **word_searched.data,
            **instagram_search.data,
            **description.data,
        }

        return Response(aggregated_data, status=status.HTTP_200_OK)