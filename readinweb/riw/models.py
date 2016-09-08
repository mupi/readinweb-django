from django.db import models
from django.utils import timezone

class Course (models.Model):
    name        = models.CharField (max_length=150)
    description = models.TextField()
    def __str__(self) :
        return self.name


class Course_class (models.Model):
    # Foreign Keys
    course          = models.ForeignKey('Course')
    instructor      = models.ForeignKey('users.User')

    title           = models.CharField(max_length=150)
    created_at      = models.DateTimeField(default=timezone.now)
    started_at      = models.DateTimeField(null=True, blank= True)
    finished_at     = models.DateTimeField(null=True, blank= True)
    enrolling       = models.BooleanField(default=False)
    max_students    = models.IntegerField(null=True, blank= True)

    class Meta:
        verbose_name_plural = "Course classes"

class Module(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) :
        return self.title

class Activity(models.Model):
    # Foreign Keys
    course          = models.ForeignKey('Course')
    module          = models.ForeignKey('Module')

    title           = models.CharField(max_length=150)
    content         = models.TextField()
    course_position = models.IntegerField(null=True, blank= True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self) :
        return self.title

class Exercise(models.Model):
    # Foreign Keys
    activity = models.ForeignKey('Activity')

    content  = models.TextField()

    class Meta:
        verbose_name_plural = "Exercises"

class Grammar(models.Model):
    # Foreign Keys
    module  = models.ForeignKey('Module')

    content = models.TextField()

    class Meta:
        verbose_name_plural = "Grammars"

class Strategy(models.Model):
    # Foreign Keys
    module  = models.ForeignKey('Module')

    content = models.TextField()
    reading = models.BooleanField()

    class Meta:
        verbose_name_plural = "Strategies"

class Functional_word(models.Model):
    # Foreign Keys
    module      = models.ForeignKey('Module')

    word        = models.CharField(max_length=50)
    meaning     = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Functional Words"


class Glossary(models.Model):
    # Foreign Keys
    module      = models.ForeignKey('Module')

    word        = models.CharField(max_length=50)
    translation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Glossaries"


class Activity_released(models.Model):
    # Foreign Keys
    course_class    = models.ForeignKey('Course_class')
    activity        = models.ForeignKey('activity')

    released        = models.BooleanField(default=False, blank= True)

    class Meta:
        verbose_name_plural = "Released Activities"

class Student_progress(models.Model):
    # Foreign Keys
    student         = models.ForeignKey('users.User')
    activity        = models.ForeignKey('Activity')
    course_class    = models.ForeignKey('Course_class')

    complete        = models.BooleanField(default=False, blank= True)

    class Meta:
        verbose_name_plural = "Students Progress"

class Allowed_student(models.Model):
    # Foreign Keys
    student         = models.ForeignKey('users.User')

    course_class    = models.ForeignKey('Course_class')
    allowed         = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name_plural = "Allowed Students"
