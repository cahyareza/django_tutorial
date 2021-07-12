from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    # Jika cookies sdah diset sebelumnya
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Wellcome back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    # Jika cookie awal diset
    else:
        value = 1
        text = 'Wellcome for the first time'
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)

    return html

# read cookies from request
# using request.COOKIE[]
def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br> You requested this page {1} times</h1></center>".format(text,value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')
