from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    print(request.user.username)
    s = 'user:' + str(request.user)
    return HttpResponse(s)
