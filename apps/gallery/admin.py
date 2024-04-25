from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

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
class ClassLessonAdmin(TranslationAdmin):
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

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


