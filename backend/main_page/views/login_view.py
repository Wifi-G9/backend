from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from backend.main_page.models import User


class LoginView(APIView):
    """
    API endpoint for user login.
    """

    def post(self, request):
        """
        Handle user login.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: JSON response with login status.
        """
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        # Verify the existence of the email in the database.
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({"error": "Incorrect email or password"}, status=status.HTTP_404_NOT_FOUND)

        # Compare the provided password with the one from the database.
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            return Response({
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Incorrect email or password"}, status=status.HTTP_401_UNAUTHORIZED)
