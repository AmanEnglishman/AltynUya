from django.db import models
from apps.user.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags



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

    def save(self, *args, **kwargs):
        self.text = strip_tags(self.text)  # Очищаем текст от HTML-тегов перед сохранением
        super().save(*args, **kwargs)


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
    image = models.ImageField(upload_to='media/pages_images/', null=True, blank=True, verbose_name='Изображение')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    category = models.ForeignKey(Category, models.DO_NOTHING, verbose_name='Страница')

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.text = strip_tags(self.text)  # Очищаем текст от HTML-тегов перед сохранением
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Редактирование и добавление страниц'
        verbose_name_plural = verbose_name


class AdmissionStudents(models.Model):
    title_head = models.CharField(max_length=255, verbose_name='Верхнее название')
    text_head = RichTextField(verbose_name='Верхний текст')
    title = models.CharField(max_length=255, verbose_name='Название')
    text = RichTextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.title_head}'
    
    class Meta:
        verbose_name = 'Прием учеников'
        verbose_name_plural = verbose_name
    



class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name
