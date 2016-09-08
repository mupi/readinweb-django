from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from readinweb.users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics

from .serializers import *
from .models import *

# Create your views here.
class CourseList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Course_classList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course_class.objects.all()
    serializer_class = Course_classSerializer

class Course_classDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Course_class.objects.all()
    serializer_class = Course_classSerializer

class ModuleList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ActivityList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ExerciseList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class GrammarList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializer

class GrammarDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Grammar.objects.all()
    serializer_class = GrammarSerializer

class StrategyList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer

class StrategyDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer

class Functional_wordList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Functional_word.objects.all()
    serializer_class = Functional_wordSerializer

class Functional_wordDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Functional_word.objects.all()
    serializer_class = Functional_wordSerializer

class GlossaryList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer

class GlossaryDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer

class Activity_releasedList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = Activity_releasedSerializer

class Activity_releasedDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = Activity_releasedSerializer

class Student_progressList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Student_progress.objects.all()
    serializer_class = Student_progressSerializer

class Student_progressDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_progress.objects.all()
    serializer_class = Student_progressSerializer

class Allowed_studentList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Allowed_student.objects.all()
    serializer_class = Allowed_studentSerializer

class Allowed_studentDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Allowed_student.objects.all()
    serializer_class = Allowed_studentSerializer
