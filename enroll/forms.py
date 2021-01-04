from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from .models import *

class SignupForm(UserCreationForm):
    password2=forms.CharField(label="conferm_password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }
class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.Textarea(attrs={'class':'form-control'})}