from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return HttpResponse("hello I am django first view")


def p_name(request):
    return render(request,'Auth_app/index.html')