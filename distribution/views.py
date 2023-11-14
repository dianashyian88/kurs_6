from django.shortcuts import render
from django.views.generic import ListView
from distribution.models import Distribution


class HomeListView(ListView):
    model = Distribution
    template_name = 'distribution/home.html'
