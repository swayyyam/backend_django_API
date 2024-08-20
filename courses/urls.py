from .views import *
from django.urls import path

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('instances/', CourseInstanceCreateAPIView.as_view(), name='course-instance-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListAPIView.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailAPIView.as_view(), name='course-instance-detail'),
]