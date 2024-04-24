from django.db import models
from apps.user.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} - {self.id}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = verbose_name


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='media/news_images/', null=True, blank=True, verbose_name='Изображение')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.title}'


class Numbers(models.Model):
    number = models.CharField(max_length=255, null=False, verbose_name='Номер')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.number}'


class Files(models.Model):
    file = models.FileField(upload_to='media/files/', verbose_name='Название файла')

    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.file.name}'


class Pages(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')
    title = models.CharField(max_length=255, null=False, verbose_name='Название')
    text = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='media/news_images/', null=True, blank=True, verbose_name='Изображение')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    category = models.ForeignKey(Category, models.DO_NOTHING, verbose_name='Страница')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Редактирование и добавление страниц'
        verbose_name_plural = verbose_name