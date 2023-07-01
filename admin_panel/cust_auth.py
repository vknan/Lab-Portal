from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        # Perform your custom authentication logic here
        if user.check_password(password):
            return user
        
        return None
