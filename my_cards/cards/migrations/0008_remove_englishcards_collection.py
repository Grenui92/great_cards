# Generated by Django 4.2 on 2023-04-16 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_cardscollections_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='englishcards',
            name='collection',
        ),
    ]
