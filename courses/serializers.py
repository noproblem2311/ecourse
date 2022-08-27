from rest_framework.serializers import ModelSerializer
from .models import Course, Tag, Lesson
from django.contrib.auth.models import AbstractUser
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = AbstractUser
#         fields = ('username', 'email', 'password', 'avatar', 'first_name', 'last_name')
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_date", "updated_date"]
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = ["id", "subject", "content", "created_date", "updated_date", "tags","image"]

