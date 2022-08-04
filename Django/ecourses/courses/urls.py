from .views import CourseViewSet, LessonViewSet

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('Courses', CourseViewSet, basename='Courses')
router.register('Lesson', LessonViewSet, basename='Lesson')
urlpatterns = [
    
  
]
urlpatterns += router.urls