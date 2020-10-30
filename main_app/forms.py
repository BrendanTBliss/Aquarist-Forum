from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Profile, Post


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Username')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class Profile_User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email' ]


class Post_Form(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title','content', 'user', 'post_date' 
        ]
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'content': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
            'post_date': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				), 
            'user': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
			}