from dataclasses import fields
from rest_framework import serializers
from .models import Profile, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'avatar', 'contact')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'profile', 'link', 'pub_date')