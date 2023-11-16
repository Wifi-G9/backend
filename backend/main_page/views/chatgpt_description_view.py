from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from openai import OpenAIAPI

API_OPENAI="https://api.openai.com/v1/chat/completions"

class ChatGPTDescription(View):

    def get(self, request: Request,word: str) -> Response:

        word_searched = request.query_params.get("search", None)
        description = self.get_gpt_description(word)

        if not description:
            return Response({"error": "Description not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"description": description}, status=status.HTTP_200_OK)
    @staticmethod
    def get_gpt_description(word: str) -> str:
        """
        Calls OpenAI GPT-3.5-turbo API to generate a description for the given word.
        :param word: str
        :return: str
        """
        client = OpenAIAPI(API_OPENAI)
        prompt = f"Describe the {word} in maximum 100 words"

        response = client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            message=[
                {"role": "user", "content": prompt}
            ]
        )

        description = response['choices'][0]['message']['content'].strip()

        return description

