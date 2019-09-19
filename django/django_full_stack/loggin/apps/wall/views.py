from django.shortcuts import render, HttpResponse, redirect
from apps.loggin_app.models  import *
from .models import *

# Create your views here.
def index(request):
    if 'userid' in request.session.keys():
        context = {
                    'user':Users.objects.get(id=request.session['userid']),
                    'post_data': Messages.objects.all(),
                    'comment_data': Comments.objects.all()
                    }
        return render(request, 'wall.html', context)
    return HttpResponse("Error: you must be signed in to access this content")

def add_message(request, method='POST'):
    Messages.objects.create(user_id=Users.objects.get(id=request.session['userid']),
                            message=request.POST['add_message']
                            )
    return redirect('/wall')
