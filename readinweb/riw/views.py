from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from readinweb.users.models import User

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework import permissions

from .serializers import *
from .models import *

# Create your views here.
class CourseList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    ordering = ('name',)

class CourseDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCompleteSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering = ('name',)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailToken(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        serialized = UserSerializer(instance = request.user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def UserRegister(request):
    serialized = UserSerializer(data = request.data)
    if serialized.is_valid():
        if (serialized.initial_data['password'] == "" or
            serialized.initial_data['email'] == "" or
            serialized.initial_data['name'] == "") :
            return Response({"error":"All the fields are necessary"}, status=status.HTTP_400_BAD_REQUEST)
        newUser = User.objects.create_user(
            email = serialized.initial_data['email'],
            username = serialized.initial_data['username'],
            password = serialized.initial_data['password'],
            name = serialized.initial_data['name']
        )
        token = Token.objects.get_or_create(user=newUser)
        return Response({"token" : token[0].key}, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class Course_classList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course_class.objects.all()
    serializer_class = Course_classSerializer
    ordering = ('id',)

class Course_classDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Course_class.objects.all()
    serializer_class = Course_classCompleteSerializer

class ModuleList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleCompleteSerializer

class ActivityList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    ordering = ('course_position',)

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

class Released_activityList(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = Released_activitySerializer

class Released_activityDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = Released_activitySerializer

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
