# Generated by Django 4.2.1 on 2023-07-22 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("times", "0010_alter_times_prons_alter_times_verbs"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="times",
            name="prons",
        ),
        migrations.RemoveField(
            model_name="times",
            name="verbs",
        ),
    ]
