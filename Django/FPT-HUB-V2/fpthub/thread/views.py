from django.shortcuts import render
from .models import Thread
from .serializers import ThreadSerializer
from rest_framework import generics


class ThreadList(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
