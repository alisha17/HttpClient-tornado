from django.shortcuts import render
from django.http import HttpResponse

def myHelloWorld(request):
    return HttpResponse("Hello World!")