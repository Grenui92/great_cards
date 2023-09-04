# Generated by Django 4.2.1 on 2023-07-22 19:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("times", "0004_alter_times_verbs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="times",
            name="verbs",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(), default=list, size=None
                ),
                default=list,
                size=None,
            ),
        ),
    ]