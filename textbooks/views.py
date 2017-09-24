from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Textbook, Exercise, Solution


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


def new_exercise(request, isbn):
    textbook = get_object_or_404(Textbook, isbn=isbn)

    if request.method == 'POST':
        page_number = request.POST['page_number']
        exercise_number = request.POST['exercise_number']
        solution = request.POST['solution']

        user = User.objects.get(username='dacksmdm')  # TODO: get the currently logged in user

        page = Page.objects.create(
            page_number=page_number,
            textbook=textbook
        )

        exercise = Exercise.objects.create(
            exercise_number=exercise_number,
            page=page,
        )

        solution_entry = Solution.objects.create(
            solution=solution,
            exercise=exercise,
            created_by=user
        )

        return redirect('views.  textbook_detail', isbn=textbook.isbn)  # TODO: redirect to the created topic page

    return render(request, 'textbooks/new_solution.html', {'textbook': textbook})
