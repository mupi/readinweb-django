# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.CourseViewSet.as_view()),
]
