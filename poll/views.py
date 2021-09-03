from django.shortcuts import render

from .forms import Createpollform
from .models import poll

# Create your views here.

def home(request):
    context = {}
    return render(request, 'poll/home.html', context)

def createpoll(request):
    context = {}
    return render(request, 'poll/createpoll.html', context)

def result(request):
    context = {}
    return render(request, 'poll/result.html', context)

def vote(request, poll_id):
    context = {}
    return render(request, 'poll/vote.html', context)

def userprofile(request , poll_id):
    context = {}
    return render(request, 'poll/userprofile.html', context)        

