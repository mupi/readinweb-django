# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from rest_framework.authtoken import views as rest_views

from . import views as models_views

urlpatterns = [
    url(r'^users/$', models_views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', models_views.UserDetail.as_view()),
    url(r'^users/register/$', models_views.UserRegister),
    url(r'^courses/$', models_views.CourseList.as_view()),
    url(r'^courses/(?P<pk>\d+)/$', models_views.CourseDetail.as_view()),
    url(r'^courses_class/$', models_views.Course_classList.as_view()),
    url(r'^courses_class/(?P<pk>\d+)/$', models_views.Course_classDetail.as_view()),
    url(r'^modules/$', models_views.ModuleList.as_view()),
    url(r'^modules/(?P<pk>\d+)/$', models_views.ModuleDetail.as_view()),
    url(r'^activities/$', models_views.ActivityList.as_view()),
    url(r'^activities/(?P<pk>\d+)/$', models_views.ActivityDetail.as_view()),
    url(r'^exercises/$', models_views.ExerciseList.as_view()),
    url(r'^exercises/(?P<pk>\d+)/$', models_views.ExerciseDetail.as_view()),
    url(r'^grammars/$', models_views.GrammarList.as_view()),
    url(r'^grammars/(?P<pk>\d+)/$', models_views.GrammarDetail.as_view()),
    url(r'^strategies/$', models_views.StrategyList.as_view()),
    url(r'^strategies/(?P<pk>\d+)/$', models_views.StrategyDetail.as_view()),
    url(r'^functional_words/$', models_views.Functional_wordList.as_view()),
    url(r'^functional_words/(?P<pk>\d+)/$', models_views.Functional_wordDetail.as_view()),
    url(r'^glossaries/$', models_views.GlossaryList.as_view()),
    url(r'^glossaries/(?P<pk>\d+)/$', models_views.GlossaryDetail.as_view()),
    url(r'^released_activities/$', models_views.Released_activityList.as_view()),
    url(r'^released_activities/(?P<pk>\d+)/$', models_views.Released_activityDetail.as_view()),
    url(r'^student_progresses/$', models_views.Student_progressList.as_view()),
    url(r'^student_progresses/(?P<pk>\d+)/$', models_views.Student_progressDetail.as_view()),
    url(r'^allowed_students/$', models_views.Allowed_studentList.as_view()),
    url(r'^allowed_students/(?P<pk>\d+)/$', models_views.Allowed_studentDetail.as_view()),

    url(r'^api-token-auth/', rest_views.obtain_auth_token),
]
