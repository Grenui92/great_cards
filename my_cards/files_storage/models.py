from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class FileType(models.Model):

    name = models.CharField(max_length=255)
    img = models.ImageField(default='icons/other.jpeg')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()

        img = Image.open(self.img.path)

        if img.height > 100 or img.width > 100:
            new_size = (100, 100)

            img.thumbnail(new_size)
            img.save(self.img.path)


class FileExtension(models.Model):

    name = models.CharField(max_length=255)
    type = models.ForeignKey(FileType, on_delete=models.CASCADE, default=1)

class File(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    file_extension = models.ForeignKey(FileExtension, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    dropbox_file_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)

