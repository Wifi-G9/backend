import os

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests

class MusicSuggestion(APIView):
    def get(self, request, *args, **kwargs):
        """
        Get top 5 music suggestions based on the provided description.

        Parameters:
        - description (str): The description for which music suggestions are requested.

        Headers:
        - 'X-RapidAPI-Key': API key for authentication.

        Returns:
        - Status Code: 200 OK
        - Body: JSON object with a 'music' key containing a list of 5 music suggestion links.
        """
        description = request.query_params.get('description', '')
        if not description:
            return Response({"error": "Description parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Call Deezer API
        headers = {
            'X-RapidAPI-Key': os.environ.get("DEEZER-KEY")#
        }
        deezer_api_url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        params = {'q': description, 'limit': 5}
        try:
            response = requests.get(deezer_api_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            music_links = [track['link'] for track in data.get('data', [])]
            return Response({"music": music_links}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)