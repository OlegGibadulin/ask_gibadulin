from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

check = True
questions = {}
for i in range(1, 20):
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

favorites_tags = ['python', 'django', 'mysql', 'perl', 'javascript', 'css', 'html', 'c++']
best_members = ['John', 'Johnny', 'Jack', 'Jackie', 'Jim', 'Jimbo', 'James']

def paginate(object_list, request):
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page

def index(request):
    cur_questions = paginate(list(questions.values()), request)
    return render(request, 'index.html', {
        'questions': cur_questions,
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def hot(request):
    cur_questions = paginate(list(questions.values()), request)
    return render(request, 'hot.html', {
        'questions': cur_questions,
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def tag(request, tag_name):
    cur_questions = paginate(list(questions.values()), request)
    return render(request, 'tag.html', {
        'questions': cur_questions,
        'tag_name': tag_name,
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def question(request, qid):
    question = questions.get(qid)
    print(answers.values())
    return render(request, 'question.html', {
        'question': question,
        'answers': answers.values(),
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def login(request):
    return render(request, 'login.html', {
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def signup(request):
    return render(request, 'signup.html', {
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

def ask(request):
    return render(request, 'ask.html', {
        'favorites_tags': favorites_tags,
        'best_members': best_members
    })

# Create your views here.
