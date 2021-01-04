from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    return render(request, 'subjects_manager/subject_list.html')