from django.shortcuts import render, HttpResponse, redirect
from apps.loggin_app.models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def regester(request, method='POST'):
#regeister Users
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    psw = request.POST["psw"]
    psw2 = request.POST["psw-repeat"]
    #validate that the info added is correct
    #verify the passwords are matching
    if psw != psw2:
        context["passwords"]="passwords do not match"
        return render(request, "error.html", context)
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(psw.encode('utf8'), salt)
    hashed_pwd = hashed_pwd.decode('utf8')
    new_user = Users.objects.create(
                                    first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    hashed_pwd = hashed_pwd,
                                    salt = salt,
                                    )
    print("User {}{} has been created".format(first_name, last_name))
    return redirect('/')


def login(request, method='POST'):
    user = Users.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        print(logged_user.first_name)
        if bcrypt.checkpw(request.POST['l_psw'].encode(), logged_user.hashed_pwd.encode()):
            request.session['userid'] = logged_user.id
            print("*"*50)
            print("user loggdin")
            return redirect('/wall')
    return redirect("/")


def success(request):
    user_id = request.session['userid']
    user = Users.objects.filter(id=user_id)
    # print(user[0].first_name)
    # context= {
    #         'first':user[0].first_name,
    #         'last':user[0].last_name
    #         }
    return redirect(request, '/wall')

def logout(request, method='POST'):
    try:
        del request.session['userid']
    except KeyError:
        pass
    return redirect('/')
