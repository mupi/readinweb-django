from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from readinweb.users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics

from .serializers import *
from .models import *

# Create your views here.
class CourseViewSet(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserViewSet(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
