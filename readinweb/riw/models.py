from django.db import models
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from rest_framework.authtoken.models import Token

'''
Auto crete a new authorization token to a new registered User
Future changes: make a renewable token that auto renews
'''
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Course (models.Model):
    name        = models.CharField (max_length=150)
    description = models.TextField()

    def __str__(self) :
        return self.name


class Course_class (models.Model):
    # Foreign Keys
    course          = models.ForeignKey('Course', related_name='course_classes')
    instructor      = models.ForeignKey('users.User')

    title           = models.CharField(max_length=150)
    created_at      = models.DateTimeField(default=timezone.now)
    started_at      = models.DateTimeField(null=True, blank= True)
    finished_at     = models.DateTimeField(null=True, blank= True)
    enrolling       = models.BooleanField(default=False)
    max_students    = models.IntegerField(null=True, blank= True)

    class Meta:
        verbose_name_plural = "Course classes"

    def __str__(self) :
        return self.course.name + " - " + self.title

class Module(models.Model):
    #Foreign Keys
    course          = models.ForeignKey('Course', related_name='modules')

    title = models.CharField(max_length=100)

    def __str__(self) :
        return self.title

class Activity(models.Model):
    # Foreign Keys
    module          = models.ForeignKey('Module', related_name='activities')

    title           = models.CharField(max_length=150)
    content         = models.TextField()
    course_position = models.IntegerField(null=True, blank= True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self) :
        return self.title

class Exercise(models.Model):
    # Foreign Keys
    activity = models.ForeignKey('Activity', related_name='exercises')

    content  = models.TextField()

    class Meta:
        verbose_name_plural = "Exercises"

class Grammar(models.Model):
    # Foreign Keys
    module  = models.ForeignKey('Module', related_name='grammars')

    content = models.TextField()

    class Meta:
        verbose_name_plural = "Grammars"

class Strategy(models.Model):
    # Foreign Keys
    module  = models.ForeignKey('Module', related_name='strategies')

    content = models.TextField()
    reading = models.BooleanField()

    class Meta:
        verbose_name_plural = "Strategies"

class Functional_word(models.Model):
    # Foreign Keys
    module      = models.ForeignKey('Module', related_name='functional_words')

    word        = models.CharField(max_length=50)
    meaning     = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Functional Words"

class Glossary(models.Model):
    # Foreign Keys
    module      = models.ForeignKey('Module', related_name='glossaries')

    word        = models.CharField(max_length=50)
    translation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Glossaries"

class Released_activity(models.Model):
    # Foreign Keys
    course_class    = models.ForeignKey('Course_class', related_name='released_activities')
    activity        = models.ForeignKey('activity', related_name='released_activities')

    released        = models.BooleanField(default=False, blank= True)

    class Meta:
        verbose_name_plural = "Released Activities"

class Student_progress(models.Model):
    # Foreign Keys
    student         = models.ForeignKey('users.User', related_name='students_progress')
    activity        = models.ForeignKey('Activity', related_name='students_progress')
    course_class    = models.ForeignKey('Course_class', related_name='students_progress')

    complete        = models.BooleanField(default=False, blank= True)

    class Meta:
        verbose_name_plural = "Students Progress"

class Allowed_student(models.Model):
    # Foreign Keys
    student         = models.ForeignKey('users.User', related_name='allowed_students')
    course_class    = models.ForeignKey('Course_class', related_name='allowed_students')

    allowed         = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name_plural = "Allowed Students"
