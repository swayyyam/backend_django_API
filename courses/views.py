from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer


class CourseListCreateAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CourseInstanceCreateAPIView(APIView):
    def post(self, request):
        serializer = CourseInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseInstanceListAPIView(APIView):
    def get(self, request, year, semester):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(instances, many=True)
        return Response(serializer.data)


class CourseInstanceDetailAPIView(APIView):
    def get(self, request, year, semester, course_id):
        instance = get_object_or_404(CourseInstance, year=year, semester=semester, course_id=course_id)
        serializer = CourseInstanceSerializer(instance)
        return Response(serializer.data)

    def delete(self, request, year, semester, course_id):
        instance = get_object_or_404(CourseInstance, year=year, semester=semester, course_id=course_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
