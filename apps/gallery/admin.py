from django.contrib import admin

from apps.gallery.models import (GalleryImages, ClassLesson)


@admin.register(GalleryImages)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )
    list_display_links = (
        'id',
        'image',
    )
    list_filter = (
        'id',
        'image',
    )
    search_fields = (
        'id',
        'image',
    )


@admin.register(ClassLesson)
class ClassLessonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'id',
        'title',
    )
    search_fields = (
        'id',
        'title',
    )
