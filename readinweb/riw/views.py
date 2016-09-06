from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

# Create your views here.
class ClassListView(ListView):
    model = Course
    # These next two lines tell the view to index lookups by username
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
