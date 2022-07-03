from re import template
from django.shortcuts import render
from rest_framework import viewsets

# from .models import CounterPost, seeds
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class= ProfileSerializer

# class ProfileDetailView():
    
#     template_name = 'home.html'
#     def counterseed(self):
#         totalseed=CounterPost.objects.filter(name=CounterPost.created_by).count()
        
#         return totalseed
    
   