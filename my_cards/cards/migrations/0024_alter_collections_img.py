# Generated by Django 4.2.1 on 2024-08-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0023_alter_cards_img_alter_collections_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='img',
            field=models.ImageField(default='collections_img/collection.webp', upload_to='collections_img'),
        ),
    ]