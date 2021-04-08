from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile



class UserUpdateForm(forms.ModelForm):  
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserprofileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['is_employer', 'image', 'phone_number']