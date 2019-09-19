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
    hashed_pwd = bcrypt.hashpw(psw.encode(), salt)
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
        if bcrypt.check_password_hash(request.POST['l_psw'].encode(), logged_user.hashed_pwd.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect("/")


def success():
    return render(request, "success.html")
