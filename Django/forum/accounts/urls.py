from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from django.urls import path
router = DefaultRouter()
router.register('Profiles',ProfileViewSet)

urlpatterns =[
    # path('seeds/',ProfileDetailView.as_view(), name='seeds')
]
urlpatterns += router.urls
