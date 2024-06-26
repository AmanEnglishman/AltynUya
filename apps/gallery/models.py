from django.db import models


class GalleryImages(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/gallery/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ClassLesson(models.Model):
    title_head = models.CharField(max_length=255, verbose_name='Верхнее название') 
    text = models.TextField(verbose_name='Текст')
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.FileField(upload_to='media/class_lessons/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Кружки'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
