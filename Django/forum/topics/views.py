from django.shortcuts import render
from .models import Topic
from .serializers import TopicSerializer
from rest_framework import generics
# Create your views here.
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

