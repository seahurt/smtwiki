from django.db import models
from django.contrib.auth.models import AbstractUser
from mdeditor.fields import MDTextField
# Create your models here.


class User(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tag')
    create_time = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    obj = models.IntegerField()
    obj_type = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    action = models.CharField(max_length=20)  # login, logout, create, delete, update
    time = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    editor = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    content = MDTextField()
