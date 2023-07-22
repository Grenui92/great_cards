from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Verbs(models.Model):
    name = models.CharField()
    pron = ArrayField(models.CharField())
    verbs = ArrayField(models.CharField())

# Create your models here.
class Times(models.Model):
    name = models.CharField(max_length=255)
    rule = models.CharField()
    examples = ArrayField(models.CharField())
    verbs = models.ManyToManyField(Verbs, db_column='verbs_id')


    

class Sentences(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)