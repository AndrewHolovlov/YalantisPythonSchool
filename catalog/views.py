from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CourseSerializer

from .models import Course


class CourseView(ListAPIView, CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ['name']
    filterset_fields = ['start_date', 'end_date']
    ordering_fields = ['start_date', 'end_date']


class SingleCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer