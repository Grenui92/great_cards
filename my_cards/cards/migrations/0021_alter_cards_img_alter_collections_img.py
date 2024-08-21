# Generated by Django 4.2.1 on 2024-08-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0020_alter_collections_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='img',
            field=models.ImageField(default='/words_img/card.jpg', upload_to='words_img'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='img',
            field=models.ImageField(default='/collections_img/collection.jpg', upload_to='collections_img'),
        ),
    ]
