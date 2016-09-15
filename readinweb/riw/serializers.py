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
    class Meta:
        model = Course
        fields = ('id', 'name', 'description',)

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'course', 'title', )

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'module', 'title', 'content', 'course_position')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'activity', 'content')

class GrammarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grammar
        fields = ('id', 'module', 'content')

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'module', 'content', 'reading')

class Functional_wordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functional_word
        fields = ('id', 'module', 'word', 'meaning')

class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Glossary
        fields = ('id', 'module', 'word', 'translation')

class Released_activitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Released_activity
        fields = ('id', 'course_class', 'activity', 'released')

class Student_progressSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Student_progress
        fields = ('id', 'student', 'activity', 'course_class', 'complete')

class Allowed_studentSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Allowed_student
        fields = ('id', 'student', 'course_class', 'allowed')

class ModuleCompleteSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    grammars = GrammarSerializer(many=True, read_only=True)
    strategies = StrategySerializer(many=True, read_only=True)
    functional_words = Functional_wordSerializer(many=True, read_only=True)
    glossaries = GlossarySerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ('id', 'title', 'activities', 'grammars', 'strategies', 'functional_words', 'glossaries')

class CourseCompleteSerializer(serializers.ModelSerializer):
    course_classes = Course_classSerializer(many=True, read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'course_classes', 'modules')

class Course_classCompleteSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    released_activities = Released_activitySerializer(many=True, read_only=True)

    class Meta:
        model = Course_class
        fields = ('id', 'course', 'instructor', 'title' ,'created_at' ,'started_at', 'finished_at', 'enrolling', 'max_students', 'released_activities')
