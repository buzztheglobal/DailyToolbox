# backend/api/utils.py
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

def get_or_create_user_from_firebase_uid(uid, decoded_token):
    """
    Retrieves a Django User based on Firebase UID.
    If the user does not exist, it creates a new one.
    """
    try:
        # Attempt to get the user by their Firebase UID
        user = User.objects.get(username=uid) # Using UID as username for simplicity
        return user
    except User.DoesNotExist:
        # If user does not exist, create a new one
        try:
            user = User.objects.create_user(
                username=uid,
                email=decoded_token.get('email', ''),
                password=None, # Firebase handles password, so Django doesn't need it
                first_name=decoded_token.get('name', '').split(' ')[0] if 'name' in decoded_token else '',
                last_name=' '.join(decoded_token.get('name', '').split(' ')[1:]) if 'name' in decoded_token and len(decoded_token.get('name', '').split(' ')) > 1 else ''
            )
            user.is_active = True # Firebase users are active by default
            user.save()
            return user
        except IntegrityError:
            # Handle race condition if another process created the user simultaneously
            return User.objects.get(username=uid)
