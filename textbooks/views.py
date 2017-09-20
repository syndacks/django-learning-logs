from django.shortcuts import render
from django.http import HttpResponse

from .models import Textbook

# Show all textbooks in the database
def index(request):
    textbooks = Textbook.objects.all()
    return render(request, 'textbooks/index.html', {'textbooks': textbooks})


# Show a single textbook by ISBN
def textbook_detail(request, isbn):
    textbook = Textbook.objects.get(isbn=isbn)
    return render(request, 'textbooks/textbook_detail.html', {'textbook': textbook})


# A static "About Me" page
def about(request):
    return render(request, 'textbooks/about.html')
