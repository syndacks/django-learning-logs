from django.shortcuts import render
from django.http import HttpResponse

from .models import Textbook

def home(request):
    textbooks = Textbook.objects.all()
    textbooks_names = list()

    for textbook in textbooks:
        textbooks_names.append(textbook.title)

    response_html = '<br>'.join(textbooks_names)
    return HttpResponse(response_html)
