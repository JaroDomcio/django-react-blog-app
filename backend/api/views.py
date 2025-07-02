from django.shortcuts import render
from .models import Post
from rest_framework import generics 
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer