# Generated by Django 4.1.2 on 2024-04-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_news_text_ky_news_text_ru_alter_news_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='pages',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]