# Generated by Django 4.1.2 on 2024-04-25 08:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_admissionstudents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admissionstudents',
            options={'verbose_name': 'Прием учеников', 'verbose_name_plural': 'Прием учеников'},
        ),
        migrations.AddField(
            model_name='admissionstudents',
            name='text',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admissionstudents',
            name='text_head',
            field=ckeditor.fields.RichTextField(verbose_name='Верхний текст'),
        ),
        migrations.AlterField(
            model_name='admissionstudents',
            name='text_head_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Верхний текст'),
        ),
        migrations.AlterField(
            model_name='admissionstudents',
            name='text_head_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Верхний текст'),
        ),
    ]
