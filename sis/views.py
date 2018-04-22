from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'sis/home.html', context_dict)


def home1(request):
    context_dict = {}
    return render(request, 'sis/home.html', context_dict)


def marks(request):
    context_dict = {}
    return render(request, 'sis/hitesh.html', context_dict)


def dac(request):
    context_dict = {}
    return render(request, 'sis/akshat.html', context_dict)


def feedback(request):
    context_dict = {}
    return render(request, 'sis/abhinav.html', context_dict)


def news(request):
    context_dict = {}
    return render(request, 'sis/tushar.html', context_dict)


def afterlogin(request):
    context_dict = {}
    return render(request, 'sis/sankalp.html', context_dict)
