from django import forms
from .models import Book

class UserForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email", max_length=100)
    password = forms.CharField(label="Your Password", max_length=100, widget=forms.PasswordInput)
    
    

