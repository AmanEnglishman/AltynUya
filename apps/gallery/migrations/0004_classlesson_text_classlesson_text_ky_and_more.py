# Generated by Django 4.1.2 on 2024-04-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_classlesson_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='text',
            field=models.TextField(default=1, verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classlesson',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='title_head',
            field=models.CharField(default=1, max_length=255, verbose_name='Верхнее название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classlesson',
            name='title_head_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхнее название'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='title_head_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхнее название'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]
