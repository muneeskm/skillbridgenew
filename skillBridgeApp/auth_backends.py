from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        identifier = username  # what user typed

        # First try username
        try:
            user = User.objects.get(username=identifier)
        except User.DoesNotExist:
            # Then try email
            try:
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                return None

        # Check password
        if user.check_password(password):
            return user

        return None