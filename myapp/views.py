
from django.shortcuts import render
from rest_framework import generics

from .models import Users
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = PostSerializer

# Create your views here.
