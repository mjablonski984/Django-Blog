from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # default django user creation form class
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # add email to register form, default UserCreationForm doesn't provide email input, (default required=True)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # fields will display in this order


# ModelForm allows to create a form that will work with specific model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # add email

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']