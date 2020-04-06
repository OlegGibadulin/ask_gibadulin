from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator

class ProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]

class Profile(models.Model):
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return self.rating

class TagManager(models.Manager):
    def popular(self):
        return self.order_by('-references_num')[:10]

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    references_num = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )

    objects = TagManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.count)

class QuestionManager(models.Manager):
    def newest(self):
        return self.filter(is_active=True).order_by('-pub_date')
    
    def hottest(self):
        return self.filter(is_active=True).order_by('-rating')

    def by_tag(self, tag_name):
        return self.filter(is_active=True, tags__name=tag_name)

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now, db_index=True)
    answers_number = models.IntegerField(
        default=0, db_index=True, validators=[MinValueValidator(0)],
    )

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(Profile, blank=True, related_name='question_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='question_dislikes')

    objects = QuestionManager()

    def __str__(self):
        return self.title

class AnswerManager(models.Manager):
    def newest_by_question(self, id):
        return self.filter(is_active=True, question=id).order_by('-pub_date')
    
    def hottest_by_question(self, id):
        return self.filter(is_active=True, question=id).order_by('-rating')

class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, blank=True, related_name='answer_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='answer_dislikes')

    objects = AnswerManager()

    def __str__(self):
        return self.text



