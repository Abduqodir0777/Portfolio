from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'job', 'username', 'email', 'phone_number', 'password1', 'password2')
