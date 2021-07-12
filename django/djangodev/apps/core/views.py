from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('dataflair', 'Hello this is your cookies', max_age = None)
    return html

# read cookies from request
# using request.COOKIE[]
def showcookie(request):
    show = request.COOKIES['dataflair']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)