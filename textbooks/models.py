from django.db import models
from django.contrib.auth.models import User


# Textbook == Board
class Textbook(models.Model):
    isbn = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    description = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    page_number = models.IntegerField(primary_key=True, unique=True)
    # a Textbook takes multiple Pages, but a Page has only one Textbook
    textbook = models.ForeignKey(Textbook, related_name='pages')


# Exercise == Topic
class Exercise(models.Model):
    exercise_number = models.CharField(max_length=4, primary_key=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    # Relational
    page = models.ForeignKey(Page, related_name='exercises')

    # not including a solution here becuase I'm not sure that it's necessary
    # solution = models.ManyToOneRel('Solution', related_name='exercises')

    # comment out 'starter' for now - eventually an Admin will be able to do this
    # starter = models.ForeignKey(User, related_name='exercises')


# Solution == Post
class Solution(models.Model):
    solution = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    # Relational
    created_by = models.ForeignKey(User, related_name='solutions')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    exercise = models.ForeignKey(Exercise, related_name='solutions')


# class User(models.Model):
#     username = models.CharField(max_length=20, primary_key=True)
#     last_name = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=20)
#     created_at = models.DateField()
