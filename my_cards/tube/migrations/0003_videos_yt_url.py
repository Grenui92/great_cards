# Generated by Django 4.2.1 on 2023-12-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_videos_yt_id_alter_videos_video_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='yt_url',
            field=models.CharField(default=1),
        ),
    ]
