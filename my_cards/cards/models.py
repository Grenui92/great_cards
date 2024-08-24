from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from PIL import Image


class Cards(models.Model):
    """The Cards class is a model class that represents a card in the
    database.

    The class has the following attributes:
    
    - english_word: a CharField that stores the English word on the card
    - russian_word: a CharField that stores the Russian translation of the word
    - word_usage: a TextField that stores the usage of the word in a sentence
    - img: an ImageField that stores the image of the card
    """

    english_word = models.CharField(max_length=255)
    russian_word = models.CharField(max_length=255)
    word_usage = models.TextField()
    img = models.ImageField(default='words_img/card.png',
                            upload_to='words_img')

    def save(self, *args, **kwargs):
        """The save function is a built-in function that saves the image to
        the database.
        The img variable opens up our image file and stores it as an Image
        object. We then check if either height or width of our image is
        greater than 50 pixels (our desired size). If so, we create a new_img
        tuple with 50 as both values and use it to resize our original img
        object using thumbnail(). Finally, we save this resized version back
        into its original path.

        :param args: Send a non-keyworded variable length argument list\
        to the function
        :param kwargs: Pass keyworded, variable-length argument list\
        to a function
        :return: None
        """
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)


class Collections(models.Model):
    """The Collections class is a model class that represents a collection.

    The class has the following attributes:
    - name: a CharField that stores the name of the collection.
    - owner: a ForeignKey that stores the owner of the collection.
    - cards: a ManyToManyField that stores the cards in the collection.
    - order_list: an ArrayField that stores the order of the cards in the\
    collection.
    - img: an ImageField that stores the image of the collection.
    """
    
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cards = models.ManyToManyField('Cards', db_column='card_id')
    order_list = ArrayField(models.IntegerField(), default=list)
    img = models.ImageField(default='collections_img/collection.webp',
                            upload_to='collections_img')

    def save(self, *args, **kwargs):
        """The save function is a built-in function that saves the image to
        the database.
        The img variable opens up our image file and stores it as an Image
        object. We then check if either height or width of our image is
        greater than 50 pixels (our desired size). If so, we create a new_img
        tuple with 50 as both values and use it to resize our original img
        object using thumbnail(). Finally, we save this resized version back
        into its original path.

        :param args: Send a non-keyworded variable length argument list\
        to the function
        :param kwargs: Pass keyworded, variable-length argument list\
        to a function
        :return: None
        """    
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)
