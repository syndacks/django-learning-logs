from django.db import models
from django.contrib.auth.models import User


# Textbook == Board
class Textbook(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField()
    author = models.CharField()
    date_published = models.DateField()
    description = models.CharField(max_length=200, blank=True)
    photo_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


# Exercise == Topic
class Exercise(models.Model):
    page_number = IntegerField()
    exercise_number = models.CharField(max_length=4)
    last_updated = models.DateTimeField(auto_now_add=True)
    # Relational
    textbook = models.ForeignKey(Textbook, related_name='exercises')
    starter = models.ForeignKey(User, related_name='exercises')


# Solution == Post
class Solution(models.Model):
    final_answer = models.TextField()
    work_steps = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    # Relational
    exercise = models.ForeignKey(Exercise, related_name='solutions')
    created_by = models.ForeignKey(User, related_name='solutions')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
