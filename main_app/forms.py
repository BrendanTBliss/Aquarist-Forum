from django.db.models.fields import CharField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, Post, Topic, Image, Comment

    
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['email',]

class Post_Form(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'topic' 
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
            'topic': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                )
        }

class Profile_User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



