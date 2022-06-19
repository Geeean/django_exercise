from django.db import models

class Question(models.Model):
  message = models.CharField(max_length=200)

