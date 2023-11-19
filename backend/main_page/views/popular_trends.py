from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from pytrends.request import TrendReq


class PopularTrends(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        """
        Function returning similar trends for a topic
        :param request: Request
        :return: Response with data: dict and status: status
        Response(
            {
                "popular_trends": [str, str, str, str, str] if found
            },
            status_code: int = 200 if word exists else 404
        )
        """
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            response = pytrends.realtime_trending_searches(pn='US')["title"][:5]
            popular_trends = [trends for trends in response]
        except KeyError:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response({"popular_trends": popular_trends}, status=status.HTTP_200_OK)
