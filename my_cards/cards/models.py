from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from PIL import Image


class Cards(models.Model):
    english_word = models.CharField(max_length=255)
    russian_word = models.CharField(max_length=255)
    word_usage = models.TextField()
    img = models.ImageField(default='golub.jpg', upload_to='words_image')

    def save(self, *args, **kwargs):
        """
        The save function is a built-in function that saves the image to the database.
        The super() function allows us to access methods from parent class, in this case,
        the save method of the Model class. The img variable opens up our image file and
        stores it as an Image object. We then check if either height or width of our image
        is greater than 50 pixels (our desired size). If so, we create a new_img tuple with
        50 as both values and use it to resize our original img object using thumbnail().
        Finally, we save this resized version back into its original path.

        :param self: Refer to the object itself.
        :param args: Send a non-keyworded variable length argument list to the function
        :param kwargs: Pass keyworded, variable-length argument list to a function
        :return: The instance of the model
        """
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)


class Collections(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cards = models.ManyToManyField('Cards', db_column='card_id')
    order_list = ArrayField(models.IntegerField(), default=list)
    img = models.ImageField(default='1.jpg', upload_to='avatars')

    def save(self, *args, **kwargs):
        """
        The save function is a built-in function that saves the image to the database.
        The super() function allows us to access methods from parent class, in this case,
        the save method of the Model class. The img variable opens up our image file and
        stores it as an Image object. We then check if either height or width of our image
        is greater than 50 pixels (our desired size). If so, we create a new_img tuple with
        50 as both values and use it to resize our original img object using thumbnail().
        Finally, we save this resized version back into its original path.

        :param self: Refer to the current instance of the class
        :param args: Send a non-keyworded variable length argument list to the function
        :param kwargs: Pass keyworded, variable-length argument list to a function
        :return: The object itself
        """
        super().save()

        img = Image.open(self.img.path)

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.img.path)
            