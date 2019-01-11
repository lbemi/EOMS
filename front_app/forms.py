from .models import Host, Services
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='',max_length=20, widget=forms.TextInput(
        attrs={'id':'username','placeholder':"用户名"}
    ))
    password = forms.CharField(label='', max_length=50,widget=forms.PasswordInput(
        attrs={'id':'password','placeholder':'密码'}
    ))
