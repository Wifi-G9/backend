from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from pytrends.request import TrendReq


class SimilarTrends(View):
    @staticmethod
    def get(request: Request) -> Response:
        """
        Function returning similar trends for a topic
        :param request: Request
        :return: Response with data: dict and status: status
        Response(
            {
                "similar_trends": [str, str, str, str, str] if found
            },
            status_code: int = 200 if word exists else 404
        )
        """
        word_searched = request.query_params.get("search", None)

        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            kw_list = [word_searched]
            pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
            similar_trends = [trends for trends in pytrends.related_topics()[word_searched]['top']['topic_title'][:5]]
        except KeyError:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response({"similar_trends": similar_trends}, status=status.HTTP_200_OK)
