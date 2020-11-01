from django.db.models.fields import CharField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, Post, Topic

    
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user']
        
        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'email']

class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username']

class Post_Form(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'image', 'topic', 'user', 'post_date' 
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
            'image': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'topic': forms.TextInput(
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

class Topic_Form(ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

class Profile_User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username']


