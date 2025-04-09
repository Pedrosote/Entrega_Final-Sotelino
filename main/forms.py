from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar
class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='Nombre')
    last_name = forms.CharField(required=True, label='Apellido')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]