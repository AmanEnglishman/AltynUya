from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe

from apps.gallery.models import (GalleryImages, ClassLesson)


@admin.register(GalleryImages)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'html_image',
    )
    list_display_links = (
        'id',
        'title',
        'html_image',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'id',
        'title',
    )
    
    def html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width='130'>")



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


