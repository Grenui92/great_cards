# Generated by Django 4.2 on 2023-04-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardsCollections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='EnglishCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_word', models.CharField(max_length=25)),
                ('russian_word', models.CharField(max_length=25)),
                ('word_usage', models.CharField(max_length=255)),
                ('collection', models.ManyToManyField(db_column='collection_id', to='cards.cardscollections')),
            ],
        ),
        migrations.AddField(
            model_name='cardscollections',
            name='cards',
            field=models.ManyToManyField(db_column='card_id', to='cards.englishcards'),
        ),
    ]
