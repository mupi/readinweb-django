from rest_framework import serializers
from readinweb.users.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'email')

class Course_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_class
        fields = ('id', 'course', 'instructor', 'title' ,'created_at' ,'started_at', 'finished_at', 'enrolling', 'max_students')

class CourseSerializer(serializers.ModelSerializer):
    course_classes = Course_classSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'course_classes')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('title',)

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('course', 'module', 'title', 'content', 'course_position')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('activity', 'content')

class GrammarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grammar
        fields = ('module', 'content')

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('module', 'content', 'reading')

class Functional_wordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functional_word
        fields = ('module', 'word', 'meaning')

class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Glossary
        fields = ('module', 'word', 'translation')

class Activity_releasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_released
        fields = ('course_class', 'activity', 'released')

class Student_progressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_progress
        fields = ('student', 'activity', 'course_class', 'complete')

class Allowed_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allowed_student
        fields = ('student', 'course_class', 'allowed')
