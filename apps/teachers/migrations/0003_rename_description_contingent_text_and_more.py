# Generated by Django 5.0.4 on 2024-04-26 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_contingent_description_ky_contingent_description_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contingent',
            old_name='description',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='contingent',
            old_name='description_ky',
            new_name='text_ky',
        ),
        migrations.RenameField(
            model_name='contingent',
            old_name='description_ru',
            new_name='text_ru',
        ),
    ]