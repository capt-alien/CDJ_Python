from django.shortcuts import render, HttpResponse, redirect

from .models import *


# Create your views here.
def index(request):
    context = {
    "books":Books.objects.all()
    }
    return render(request, "books_authors_app/index.html", context)

def process_book(request, method='POST'):
    new_book = Books.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect("/")

def view_book(request, id):
    context = {'book':Books.objects.get(id=id)}
    return render(request, "books_authors_app/book.html", context)

def view_authors(request):
    context = {
    "authors":Authors.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def process_new_author(request, method='POST'):
    new_author = Authors.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")


def view_author(request, id):
    context={'author': Authors.objects.get(id=id)}
    return render(request, "books_authors_app/author.html", context)
