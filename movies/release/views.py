from django.shortcuts import render, HttpResponse

# Create your views here.


def add(request):
    print('DATA')
    return HttpResponse('<h1>DATA DONE<h1>')
