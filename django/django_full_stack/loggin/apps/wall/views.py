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


def add_comment(request, method='POST'):
    message_id= Messages.objects.get(id=request.POST['message_id'])
    user = Users.objects.get(id=request.session['userid'])
    comment = request.POST['comment']
    Comments.objects.create(message_id=message_id,
                            user_id=user,
                            comment=comment)
    return redirect('/wall')
