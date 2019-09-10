from django.shortcuts import render
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    context = {
        "time":strftime("%H:%M %p", localtime()),
        "date":strftime("%Y-%m-%d", localtime()),
    }
    print("*"*50)
    print(context["time"])
    print(context["date"])

    return render(request, 'clock/index.html',context)
