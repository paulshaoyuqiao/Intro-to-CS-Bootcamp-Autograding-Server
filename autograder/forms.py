from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='New Password')
    email_address = forms.CharField(label='Email Address')
