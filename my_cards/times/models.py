from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Times(models.Model):
    name = models.CharField(max_length=255)
    rule = models.CharField()


class Sentences(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)