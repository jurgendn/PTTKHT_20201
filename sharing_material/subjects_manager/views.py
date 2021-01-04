from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Subjects
# Create your views here.


def index(request):
    subject_list = Subjects.objects.all()
    context = {
        "subjects": subject_list,
    }
    return render(request, 'subjects_manager/subject_list.html', context=context)