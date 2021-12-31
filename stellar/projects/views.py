from django.shortcuts import render
from django.http import HttpResponse
from . import views


def projects(request):
    return render(request, 'projects/projects.html')

