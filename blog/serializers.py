from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import exceptions, serializers
from django.contrib.auth import authenticate
from .models import Blog,Comment,Tags,Likes
from django.contrib.auth.models import User
from rest_framework import serializers



class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username is taken")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        exclude = ['created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields=['id','name']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags=TagSerializer(read_only=True)

    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at']
        

class LikesSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    blog_title = serializers.CharField(source='blog.title', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    blog_id = serializers.PrimaryKeyRelatedField(source='blog', queryset=Blog.objects.all())

    class Meta:
        model = Likes
        fields = ['id', 'user_id', 'user_name', 'blog_id', 'blog_title']


