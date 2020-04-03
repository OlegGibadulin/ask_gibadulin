from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

check = True
questions = {}
for i in range(1, 40):
    answers = {}
    questions.update({i: {
        'title': f'Title #{i}',
        'text': f'Text #{i}',
        'id': i,
        'answers_count': 2,
        'rating': i * 100,
        'tags': ['python', 'django', 'bootstrap', 'html']
    }})

answers = {}
for j in range(1, 3):
    check = not check
    answers.update({j: {
        'text': f'Answer #{j} of question',
        'rating': j * 100,
        'correct_answer': check
    }})



def paginate(object_list, request):
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page

def index(request):
    print(list(questions.keys()))
    cur_questions = paginate(list(questions.values()), request)
    print(cur_questions)
    print("!!!!!!!!!!\n")
    return render(request, 'index.html', {
        'questions': cur_questions
    })

def hot(request):
    return render(request, 'hot.html', {
        'questions': questions.values()
    })

def tag(request, tag_name):
    return render(request, 'tag.html', {
        'questions': questions.values(),
        'tag_name': tag_name
    })

def question(request, qid):
    question = questions.get(qid)
    print(answers.values())
    return render(request, 'question.html', {
        'question': question,
        'answers': answers.values()
    })

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def ask(request):
    return render(request, 'ask.html', {})

# Create your views here.
