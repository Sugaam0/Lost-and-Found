from django import forms
from .models import FoundItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# board/forms.py
class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'location', 'date_found', 'status', 'contact_info', 'image']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
