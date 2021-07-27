from rest_framework import serializers
from app1.models import Post

class PostSerializer(serializers.ModelSerializer):
    title=serializers.CharField()
    category=serializers.CharField()
    summary=serializers.CharField()
    image =serializers.ImageField()
    content=serializers.CharField()
    author=serializers.CharField()
    slug=serializers.CharField()
    draft=serializers.CharField()
    class Meta:
        model=Post
        fields = ['title','image','category','summary','content','author','slug','draft']