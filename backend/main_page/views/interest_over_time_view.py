from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from pytrends.request import TrendReq
from datetime import date, timedelta, datetime


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

        weeks = 52 if time_of_interest is not None and time_of_interest == "year" else 4

        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            pytrends.build_payload(kw_list=[word_searched],
                                   timeframe=f'{date.today() - timedelta(weeks=weeks)} {date.today()}')
            response = pytrends.interest_over_time_(word_searched)  # [word_searched]
            interest_over_time = [interest for interest in response]
        except KeyError:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        if time_of_interest == "month":
            date_list = [datetime.now() - timedelta(days=30 * i) for i in range(12)]
        else:
            date_list = [datetime.now() - timedelta(days=30 * 12 * i) for i in range(6)]
        formatted_dates = [ddate.strftime('%Y-%m-%d') for ddate in date_list]

        response_data = [{"interest": interest, "date": current_date} for interest, current_date in
                         zip(interest_over_time, formatted_dates)]

        return Response({"interest_over_time": response_data}, status=status.HTTP_200_OK)
