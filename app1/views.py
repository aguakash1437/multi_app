from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_app1(request):
    return HttpResponse('<h3>welcome to app1</h3>')

def second_app1(request):
    return HttpResponse('<h2>welcome to second app1</h2>')