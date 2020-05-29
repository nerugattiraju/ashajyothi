from django import forms
from django.contrib.auth.models import User
from .models import Content1
from .models import Document,Data
# Create your models here.
class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email","first_name","last_name"]
class DocumentForm(forms.ModelForm):
    class Meta:
        model= Document
        fields = ['description','document']
class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=["data"]

