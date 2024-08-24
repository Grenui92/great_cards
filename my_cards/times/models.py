from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Verbs(models.Model):
    """A class to represent a verb.

    The class has the following attributes:
    
    - name (str): The name of the verb.
    - pron (list): A list of pronunciations of the verb.
    - verbs (list): A list of verbs that are similar to the verb.
    """

    name = models.CharField()
    pron = ArrayField(models.CharField())
    verbs = ArrayField(models.CharField())


class Times(models.Model):
    """A class to represent a time.

    The class has the following attributes:
    
    - name (str): The name of the time.
    - rule (str): The rule for the time.
    - examples (list): A list of examples for the time.
    - verbs (list): A list of verbs that are used with the time.
    """

    name = models.CharField(max_length=255)
    rule = models.CharField()
    examples = ArrayField(models.CharField())
    verbs = models.ManyToManyField(Verbs, db_column='verbs_id')


class Sentences(models.Model):
    """A class to represent a sentence.

    The class has the following attributes:
    
    - text (str): The text of the sentence.
    - owner (User): The owner of the sentence.
    - time (Times): The time of the sentence.
    """

    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)
