from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request):
    return render(request, 'index.html', {})

def question(request):
    return render(request, 'question.html', {})

def ask(request):
    return render(request, 'ask.html', {})

# Create your views here.
