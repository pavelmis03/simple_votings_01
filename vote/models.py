from django.db import models
from django.contrib.auth.models import User

#-------------------------------------------------#
# Обязательно к ознакомлению:                     #
# https://dbdiagram.io/d/5e0b5b31edf08a25543f8603 #
#-------------------------------------------------#

class Constants:
    # КОНСТАНТЫ
    COMPLAINTS_TITLE_SIZE = 100
    COMPLAINTS_TEXT_SIZE = 500
    COMPLAINTS_STATUS = (
        ('U', 'under_consideration'),
        ('R', 'rejected'),
        ('A', 'accepted'),
    )
    POSTS_TITLE_SIZE = 100
    POSTS_DESC_SIZE = 500
    ANSWERS_TEXT_SIZE = 500


class Complaints(models.Model):
    # ЖАЛОБЫ
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=Constants.COMPLAINTS_STATUS)
    title = models.CharField(max_length=Constants.COMPLAINTS_TITLE_SIZE)
    text = models.CharField(max_length=Constants.COMPLAINTS_TEXT_SIZE)
    created_at = models.DateTimeField()


class Posts(models.Model):
    # ПОСТЫ
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # only one - true, several choices - false
    type = models.BooleanField()
    title = models.CharField(max_length=Constants.POSTS_TITLE_SIZE)
    description = models.CharField(max_length=Constants.POSTS_DESC_SIZE)
    created_at = models.DateTimeField()


class Answers(models.Model):
    # ВОЗМОЖНЫЕ ОТВЕТЫ
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.CharField(max_length=Constants.ANSWERS_TEXT_SIZE)

class Votes(models.Model):
    # ГОЛОСА
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    date = models.DateTimeField()