# Generated by Django 4.1.2 on 2024-04-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_pages_text_ky_pages_text_ru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pages_images/', verbose_name='Изображение'),
        ),
    ]
