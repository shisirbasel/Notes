from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class AddNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','content']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control mb-5'}),
            'content' : forms.Textarea(attrs={'class':'form-control mb-5'})
        }