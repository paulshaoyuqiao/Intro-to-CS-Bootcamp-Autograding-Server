from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(null=False)
    total_points = models.IntegerField()

class Submission(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=10)
    submitted_by = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(Assignment, related_name='assignments', on_delete=models.CASCADE)
    score = models.IntegerField()
