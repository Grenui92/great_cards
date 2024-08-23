from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
import re


class Videos(models.Model):
    """A class that represents the video model.

    Attributes:
        video_name (str): The name of the video.
        owner (User): The owner of the video.
        video_prev (ImageField): The preview of the video.
        video_subs (FileField): The subtitles of the video.
        yt_id (str): The YouTube ID of the video.
        yt_url (str): The URL of the video.
    """

    video_name = models.CharField(max_length=255, null=True)
    owner = models.ManyToManyField(User, db_column='owner_id')
    video_prev = models.ImageField(max_length=255, default=1)
    video_subs = models.FileField(max_length=255, default=1)
    yt_id = models.CharField(max_length=255, default=1)
    yt_url = models.CharField(max_length=255, default=1)

    def save(self, *args, **kwargs):
        """Save the video preview and subtitles. Resize the preview image
        and remove the tags from the subtitles file.
        """
        super().save()
        absolute_img_path = str(settings.BASE_DIR) + self.video_prev.url
        absolute_subs_path = str(settings.BASE_DIR) + self.video_subs.url

        img = Image.open(absolute_img_path)
        if img.height > 100 or img.width > 100:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(absolute_img_path)

        with open(absolute_subs_path, 'r+') as subs:
            data = subs.read()
            subs.seek(0)
            subs.truncate()

        with open(absolute_subs_path, 'w+') as subs:
            result = re.sub(r'<\S+>', '', data)
            subs.write(result)
