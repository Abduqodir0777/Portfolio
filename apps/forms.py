from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    job = forms.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'job', 'username', 'email', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone_number

    def clean_username(self):
        username = self.cleaned_data['username']
        if any(char.isdigit() for char in username):
            raise forms.ValidationError("Username should not contain digits.")
        return username