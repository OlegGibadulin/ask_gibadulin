from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from app.models import Profile, Tag, Question, Answer

def paginate(object_list, request):
    paginator = Paginator(list(object_list), 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.get_page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page

context = {
    'popular_tags': Tag.objects.popular(),
    'best_members': Profile.objects.best(),
}

def index(request):
    newest_questions = Question.objects.newest()
    context['questions'] = paginate(newest_questions, request)
    return render(request, 'index.html', context)

def hot(request):
    hottest_questions = Question.objects.hottest()
    context['questions'] = paginate(hottest_questions, request)
    return render(request, 'hot.html', context)

def tag(request, tag_name):
    questions_by_tag = Question.objects.by_tag(tag_name)
    context['questions'] = paginate(questions_by_tag, request)
    context['tag_name'] = tag_name
    return render(request, 'tag.html', context)

def question(request, qid):
    context['question'] = Question.objects.get(pk=qid)
    context['answers'] = Answer.objects.hottest_by_question(qid)
    return render(request, 'question.html', context)

def login(request):
    return render(request, 'login.html', context)

def signup(request):
    return render(request, 'signup.html', context)

def ask(request):
    return render(request, 'ask.html', context)
