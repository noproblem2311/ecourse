from django.urls import path
from .views import ThreadList

urlpatterns = [
    path("threads/",ThreadList.as_view(), name="thread_list")
]