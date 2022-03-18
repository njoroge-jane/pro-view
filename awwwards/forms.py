from django import forms
from .models import Post,Profile
#......
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        exclude = ['user']       
