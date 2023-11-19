from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from pytrends.request import TrendReq
from datetime import date, timedelta


class InterestOverTime(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        """
        Function returning interest over time for a topic
        :param request: Request
        :return: Response with data: dict and status: status
        Response(
            {
                "interest_over_time": [int * ~number_of_days] if exists
            },
            status_code: int = 200 if word exists else 404
        )
        """
        word_searched = request.query_params.get("search", None)
        time_of_interest = request.query_params.get("time", None)

        weeks = 12 if time_of_interest is not None and time_of_interest == "year" else 4

        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            pytrends.build_payload(kw_list=[word_searched],
                                   timeframe=f'{date.today() - timedelta(weeks=weeks)} {date.today()}')
            response = pytrends.interest_over_time()[word_searched]
            interest_over_time = [interest for interest in response]
        except KeyError:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response({"interest_over_time": interest_over_time}, status=status.HTTP_200_OK)
