from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context_dict = {}
    return render(request,'sis/base.html',context_dict)

def home1(request):
    context_dict = {}
    return render(request,'sis/home.html',context_dict)