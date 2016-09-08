# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^courses/$', views.CourseList.as_view()),
    url(r'^courses/(?P<pk>\d+)/$', views.CourseDetail.as_view()),
    url(r'^courses_class/$', views.Course_classList.as_view()),
    url(r'^courses_class/(?P<pk>\d+)/$', views.Course_classDetail.as_view()),
    url(r'^modules/$', views.ModuleList.as_view()),
    url(r'^modules/(?P<pk>\d+)/$', views.ModuleDetail.as_view()),
    url(r'^activities/$', views.ActivityList.as_view()),
    url(r'^activities/(?P<pk>\d+)/$', views.ActivityDetail.as_view()),
    url(r'^exercises/$', views.ExerciseList.as_view()),
    url(r'^exercises/(?P<pk>\d+)/$', views.ExerciseDetail.as_view()),
    url(r'^grammars/$', views.GrammarList.as_view()),
    url(r'^grammars/(?P<pk>\d+)/$', views.GrammarDetail.as_view()),
    url(r'^strategies/$', views.StrategyList.as_view()),
    url(r'^strategies/(?P<pk>\d+)/$', views.StrategyDetail.as_view()),
    url(r'^functional_words/$', views.Functional_wordList.as_view()),
    url(r'^functional_words/(?P<pk>\d+)/$', views.Functional_wordDetail.as_view()),
    url(r'^glossaries/$', views.GlossaryList.as_view()),
    url(r'^glossaries/(?P<pk>\d+)/$', views.GlossaryDetail.as_view()),
    url(r'^activities_released/$', views.Activity_releasedList.as_view()),
    url(r'^activities_released/(?P<pk>\d+)/$', views.Activity_releasedDetail.as_view()),
    url(r'^student_progresses/$', views.Student_progressList.as_view()),
    url(r'^student_progresses/(?P<pk>\d+)/$', views.Student_progressDetail.as_view()),
    url(r'^allowed_students/$', views.Allowed_studentList.as_view()),
    url(r'^allowed_students/(?P<pk>\d+)/$', views.Allowed_studentDetail.as_view()),

]
