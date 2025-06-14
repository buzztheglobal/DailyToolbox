# backend/core/firebase_config.py
import firebase_admin  # type: ignore
from firebase_admin import credentials, auth
import os

# Path to your service account key file
# Ensure this path is correct relative to your manage.py file or Django project root
SERVICE_ACCOUNT_KEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'serviceAccountKey.json')

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized successfully.")
    except Exception as e:
        print(f"Error initializing Firebase Admin SDK: {e}")
        print(f"Expected service account key at: {SERVICE_ACCOUNT_KEY_PATH}")

def verify_firebase_token(id_token):
    """
    Verifies a Firebase ID token.
    Returns the decoded token (dict) if valid, None otherwise.
    """
    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Firebase token verification failed: {e}")
        return None
