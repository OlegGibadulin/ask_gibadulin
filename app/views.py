from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def get_questions():
    questions = {}
    for i in range(1, 30):
        questions.update({i: {
            'title': f'Title #{i}',
            'text': f'Text #{i}',
            'id': i
        }})
    return questions

def index(request):
    return render(request, 'index.html', {
        'questions': get_questions().values()
    })

def hot(request):
    return render(request, 'index.html', {})

def tag(request, tag_name):
    return render(request, 'index.html', {})

def question(request, qid):
    question = get_questions().get(qid)
    return render(request, 'question.html', {
        'question': question
    })

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def ask(request):
    return render(request, 'ask.html', {})

# Create your views here.
