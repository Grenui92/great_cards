# Generated by Django 4.2.1 on 2024-01-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0014_remove_videos_video_audi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='video_path',
        ),
    ]
