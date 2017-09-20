from django.shortcuts import render
from django.http import HttpResponse

from .models import Textbook


def about(request):
    return render(request, 'textbooks/about.html')


def index(request):
    textbooks = Textbook.objects.all()
    return render(request, 'textbooks/index.html', {'textbooks': textbooks})
