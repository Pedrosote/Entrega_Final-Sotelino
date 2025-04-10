# mensajes/forms.py
from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(
        queryset=User.objects.all().exclude(is_superuser=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})
        }
