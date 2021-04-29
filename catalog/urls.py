from django.urls import path

from .views import CourseView, SingleCourseView


app_name = 'catalog'

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:pk>', SingleCourseView.as_view())
]