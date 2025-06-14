# backend/api/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from firebase_admin import auth # type: ignore
from django.conf import settings
from .utils import get_or_create_user_from_firebase_uid

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if not auth_header:
            return None # No authentication header provided

        try:
            # Expect 'Bearer <token>'
            id_token = auth_header.split(' ').pop()
            decoded_token = auth.verify_id_token(id_token)

            # Get the UID from the decoded token
            uid = decoded_token['uid']

            # Retrieve or create a Django user corresponding to the Firebase UID
            user = get_or_create_user_from_firebase_uid(uid, decoded_token)

            return (user, None) # authentication successful, return (user, auth)
        except Exception as e:
            print(f"Firebase Authentication Failed: {e}")
            raise AuthenticationFailed('Invalid Firebase ID token or user does not exist.')
