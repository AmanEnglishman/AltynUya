from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import strip_tags

from apps.news.models import Numbers


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    image = models.ImageField(upload_to='media/teachers/', verbose_name='Фотография')
    job_title = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Преподователи'
        verbose_name_plural = verbose_name


class Vacancy(models.Model):
    job_title = models.CharField(max_length=255, verbose_name='Должность')
    duty = models.CharField(max_length=255, verbose_name='Обязанность')
    requirements = models.CharField(max_length=255, verbose_name='Требования')
    conditions = models.CharField(max_length=255, verbose_name='Условия')
    number = models.ForeignKey(Numbers, models.SET_NULL, null=True, verbose_name='Контакт')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = verbose_name


class Qualification(models.Model):
    teacher = models.ForeignKey(Teacher, models.SET_NULL, null=True, verbose_name='Преподавтель')
    image = models.ImageField(upload_to='media/qualification/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.teacher.name

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = verbose_name


class Contingent(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    text = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='media/contingent/', verbose_name='Фотография')
    grade = models.CharField(max_length=100, verbose_name='Класс')

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.text = strip_tags(self.text)  # Очищаем текст от HTML-тегов перед сохранением
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Контингент'
        verbose_name_plural = verbose_name

    
