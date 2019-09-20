from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from apps.walla.models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def regester(request, method='POST'):
#regeister User
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    psw = request.POST["psw"]
    psw2 = request.POST["psw-repeat"]
    if psw != psw2:
        context["passwords"]="passwords do not match"
        return render(request, "error.html", context)
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(psw.encode('utf8'), salt)
    hashed_pwd = hashed_pwd.decode('utf8')
    new_user = User.objects.create(
                                    first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    hashed_pwd = hashed_pwd,
                                    )
    print("User {}{} has been created".format(first_name, last_name))
    return redirect('/')


def login(request, method='POST'):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        print(logged_user.first_name)
        if bcrypt.checkpw(request.POST['l_psw'].encode(), logged_user.hashed_pwd.encode()):
            request.session['userid'] = logged_user.id
            print("*"*50)
            print("user loggdin")
            return redirect('/wall')
    return redirect("/")


def wall(request):
    if 'userid' in request.session.keys():
        context = {
                    'user':User.objects.get(id=request.session['userid']),
                    'post_data': Messages.objects.all(),
                    'comment_data': Comments.objects.all()
                    }
        print(Comments.objects.all())
        return render(request, 'wall.html', context)
    return HttpResponse("Error: you must be signed in to access this content")


def logout(request, method='POST'):
    try:
        del request.session['userid']
    except KeyError:
        pass
    return redirect('/')


def add_message(request, method='POST'):
    Messages.objects.create(user=User.objects.get(id=request.session['userid']),
                            message=request.POST['add_message']
                            )
    return redirect('/wall')


def add_comment(request, method='POST'):
    message_id= Messages.objects.get(id=request.POST['message_id'])
    user = User.objects.get(id=request.session['userid'])
    comment = request.POST['comment']
    Comments.objects.create(message=message_id,
                            user=user,
                            comment=comment)
    return redirect('/wall')


def delete_message(request, id):
    deleter = Messages.objects.get(id=id)
    deleter.delete()
    return redirect('/wall')
