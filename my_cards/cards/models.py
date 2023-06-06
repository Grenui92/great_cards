from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class EnglishCards(models.Model):
    english_word = models.CharField(max_length=25)
    russian_word = models.CharField(max_length=25)
    word_usage = models.TextField()
    img = models.ImageField(default='golub.jpg', upload_to='words_image')

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)


class CardsCollections(models.Model):
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cards = models.ManyToManyField('EnglishCards', db_column='card_id')
    img = models.ImageField(default='1.png', upload_to='avatars')

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)
