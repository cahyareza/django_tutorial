from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, 'base.html')

def other(request):
    context = {
        'k1': 'wellcome to the second page',
    }
    return render(request, 'others.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html',{'time': time})