from django import forms
from .models import Image,Profile
#......
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date','comments','likes']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        exclude = ['user']       
