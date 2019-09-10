from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("This is a page for new posts")

def create(request):
    return  redirect("/")

def display(request, id):
    return HttpResponse("display post "+id)

def edit(request, id):
    return HttpResponse("Edit Post #"+ id)

def destroy(request, id):
    return HttpResponse("Delete Post #"+ id)
