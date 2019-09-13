from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    #needs to querry all books in the DB and display on the right of the screen
    #
    return render(request, "books_authors_app/index.html")


def process_book(request):
    pass



def view_authors(request):
    pass



def submitt_new_author(request):
    pass
