from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from urllib.parse import unquote
from django.shortcuts import redirect

User = get_user_model()


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username is an email address
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            
            # Check the password
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        # Redirect authenticated users to the dashboard
        if user and user.is_authenticated:
            return user.is_active
        return False

    def authentication_failed(self, request, message=None, **kwargs):
        # Redirect users to the login page with an error message
        error_message = unquote(request.GET.get('error_message', ''))
        return redirect(f'/login/?error_message={error_message}')