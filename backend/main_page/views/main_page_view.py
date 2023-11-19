from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main_page.views.sentiment_analysis_view import SentimentAnalysis
from main_page.views.word_search_view import WordSearch
from main_page.views.instagram_search_view import InstagramSearch
from main_page.views.similar_trends_view import SimilarTrends
from main_page.views.popular_trends_view import PopularTrends
from main_page.views.interest_over_time_view import InterestOverTime
from main_page.views.chatgpt_description_view import ChatGPTDescription


class MainPageView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        word_searched: Response = WordSearch.as_view()(request)
        instagram_search: Response = InstagramSearch.as_view()(request)
        similar_trends: Response = SimilarTrends.as_view()(request)
        popular_trends: Response = PopularTrends.as_view()(request)
        interest_over_time: Response = InterestOverTime.as_view()(request)
        sentiment_analysis: Response = SentimentAnalysis.as_view()(request)
        chatgpt_description: Response = ChatGPTDescription.as_view()(request)

        aggregated_data = {
            **word_searched.data,
            **instagram_search.data,
            **chatgpt_description.data,
            **similar_trends.data,
            **popular_trends.data,
            **interest_over_time.data,
            **sentiment_analysis.data,
        }

        return Response(aggregated_data, status=status.HTTP_200_OK)
