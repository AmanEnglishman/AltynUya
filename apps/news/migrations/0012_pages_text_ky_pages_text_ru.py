# Generated by Django 4.1.2 on 2024-04-24 06:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_pages_title_ky_pages_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='pages',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст'),
        ),
    ]
