from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<H1>Data Flair Django</h1>Hello, you just configured your first URL")

def data_flair(request):
    return redirect('/dataflair')