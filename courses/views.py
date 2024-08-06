from django.shortcuts import render
from  .models import Courses
from .serialiser import CoursesSerializer

# from rest_framework import generics
# from generics import CreateApiView ,ListAPIView, RetrieveAPIView, DestroyAPIView

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permissions_classes=(AllowAny,)

# class CoursesView(ListAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
#     permissions_classes=(IsAuthenticatedOrReadOnly,)

# class CoursesDetailView(RetrieveAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
#     permissions_classes=(IsAuthenticatedOrReadOnly,)

# class CoursesCreateView(CreateAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
#     permissions_classes=(IsAuthenticatedOrReadOnly,)

# class CoursesDeleteView(DestroyAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
#     permissions_classes=(IsAuthenticatedOrReadOnly,)


