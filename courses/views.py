from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import CourseSerializer, LessonSerializer
from .models import Course, Lesson
# from django.contrib.auth.models import AbstractUser

# Create your views here.

# class UserViewSet(viewsets.ViewSet, 
#                   generics.CreateAPIView,
#                   generics.RetrieveAPIView):
#     queryset = AbstractUser.objects.filter(is_active=True)
#     serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    # tao api de an 1 khoa hoc
    @action(methods=['post'], 
            detail=True, 
            url_path="hide-lessons", 
            url_name="hide-lessons"
            )
    def hide_lessons(self, request, pk):
        try:
            l= Lesson.objects.get(pk=pk)
            l.active=False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)
        
        return Response(data=LessonSerializer(l, context={'request':request}).data,
                        status=HTTP_200_OK
        )
