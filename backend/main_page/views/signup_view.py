from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class SignupView(APIView):
    @staticmethod
    def post(self, request):
        # Extract necessary fields from headers
        username = request.data.get("username", "")
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        verify_password = request.data.get("verify_password", "")

        # Bare minimum field verification
        if password != verify_password:
            return Response({"error": "The password doesn't match"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify email format (example: gmail or yahoo)
        if "gmail" not in email and "yahoo" not in email:
            return Response({"error": "Invalid email format. Only Gmail and Yahoo are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        # Additional username validations
        if len(username) > 10:
            return Response({'error': "Username not longer than 10 characters!"}, status=status.HTTP_400_BAD_REQUEST)

        if not username.isalnum():
            return Response({'error': "Only numbers and letters are allowed in the username!"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if email is unique
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already in use"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username is already in use"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username, email, password)
        user.is_active = True  # Automatically activate the user without confirmation email
        user.set_password(password)
        user.save()

        return Response({"success": "User successfully signed up"}, status=status.HTTP_200_OK)
