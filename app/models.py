from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=20, verbose_name='User nickname', unique=True)
    rating = models.IntegerField(default=0, verbose_name='User rating')
    # avatar

    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name, self.rating)

class Tag(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Tag name', unique=True, db_index=True
    )
    count = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name='References number'
    )

    def __str__(self):
        return '{} {}'.format(self.name, self.count)

class QuestionManager(models.Manager):
    def get_by_date(self):
        return self.filter(is_active=True).order_by("-pub_date")
    
    def get_by_rating(self):
        return self.filter(is_active=True).order_by("-rating")

    def get_by_tag(self, tag):
        return self.filter(is_active=True, tags__name=tag)

class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name='Question title')
    text = models.TextField(verbose_name='Question text')
    rating = models.IntegerField(
        default=0, verbose_name='Diff between like and dislike', db_index=True
    )
    is_active = models.BooleanField(default=True, verbose_name='Is published question')
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Publication time',
        db_index=True
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Question author',
        related_name='Questions'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='Question tags',
        related_name='Questions'
    )
    like = models.ManyToManyField(
        Profile, blank=True, verbose_name='Likes', related_name='Questions_likes'
    )
    dislike = models.ManyToManyField(
        Profile, blank=True, verbose_name='Dislikes', related_name='Questions_dislikes'
    )

    objects = QuestionManager()

    def __str__(self):
        return self.title

class AnswerManager(models.Manager):
    def get_by_question_id(self, id):
        return self.filter(is_active=True, question=id)
    
    def get_by_question_id_by_rating(self, id):
        return self.filter(is_active=True, question=id).order_by("-rating")

class Answer(models.Model):
    text = models.TextField(verbose_name='Answer text')
    is_correct = models.BooleanField(default=False, verbose_name='Is correct answer')
    rating = models.IntegerField(default=0, verbose_name='Diff between like and dislike')
    is_active = models.BooleanField(default=True, verbose_name='Is published answer')
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Publication time'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Question',
        related_name='Answers'
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Question',
        related_name='Answers'
    )
    like = models.ManyToManyField(
        Profile, blank=True, verbose_name='Likes', related_name='Answers_likes'
    )
    dislike = models.ManyToManyField(
        Profile, blank=True, verbose_name='Dislikes', related_name='Answers_dislikes'
    )

    objects = AnswerManager()

    def __str__(self):
        return self.text

    # class Meta:
    #     order_with_respect_to = 'question'



