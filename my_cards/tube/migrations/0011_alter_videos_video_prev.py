# Generated by Django 4.2.1 on 2023-12-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0010_alter_videos_video_prev_alter_videos_video_subs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_prev',
            field=models.CharField(default=1, max_length=255),
        ),
    ]
