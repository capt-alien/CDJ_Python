from django.shortcuts import render, HttpResponse, redirect

from .models import *


# Create your views here.
def index(request):
    #needs to querry all books in the DB and display on the right of the screen
    context = {
    "books":Books.objects.all()
    }
    # context = obj.__dict__
    print("*"*50)
    print(context['books'].values())
    return render(request, "books_authors_app/index.html", context)

def process_book(request, method='POST'):
    return redirect("/")

def view_book(request, id):
    context={   'title': "testy Mctestface and the ultmate test",
                'description': "testy faceses his biggest test ever.....Django Routeing...",
                'authors': "Testy McQueen"}
    return render(request, "books_authors_app/book.html", context)

def view_authors(request):
    return HttpResponse("view authors werk")

def process_new_author(request, method='POST'):
    return HttpResponse("new box werk")

def view_author(request, id):
    return HttpResponse("view authors werk")
