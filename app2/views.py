from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_first(request):
    return HttpResponse('<h3><center>welcome to app2_first</center></h3>')

def app2_second(request):
    return HttpResponse('<h3><marquee>welcome to app2_second</marquee></h3>')

