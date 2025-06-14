from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication # Import if needed for Admin/CSRF
from .authentication import FirebaseAuthentication # Import your custom authentication

# Initialize Firebase Admin SDK when Django starts, important for global access
# This will run only once when the Django process starts
# Make sure firebase_config is imported so the initialization code runs
from core import firebase_config


@api_view(['GET'])
def health_check(request):
    """
    Returns a success message to confirm the API is running.
    """
    return Response(
        {"message": "Backend is running and connected to React!"},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@authentication_classes([FirebaseAuthentication]) # Use your custom authentication
@permission_classes([IsAuthenticated]) # Require user to be authenticated
def protected_data(request):
    """
    Returns sensitive data only if the user is authenticated via Firebase.
    """
    # request.user will be the Django user object returned by FirebaseAuthentication
    user_email = request.user.email if request.user.email else request.user.username
    return Response(
        {"message": f"Welcome, {user_email}! This is protected data.", "user_uid": request.user.username},
        status=status.HTTP_200_OK
    )
