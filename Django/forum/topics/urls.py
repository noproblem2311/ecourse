from .views import TopicList
from django.urls import path

urlpatterns=[

    path('Topics/',TopicList.as_view())
]