from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.news.models import (News, Numbers, Files, Category, Pages, AdmissionStudents, Contact)

@admin.register(News)
class NewsAdmin(TranslationAdmin):
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


@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
    )
    list_display_links = (
        'id',
        'number',
    )
    list_filter = (
        'id',
        'number',
    )
    search_fields = (
        'id',
        'number',
    )


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
    )
    list_display_links = (
        'id',
        'file',
    )
    list_filter = (
        'id',
        'file',
    )
    search_fields = (
        'id',
        'file',
    )


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
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


@admin.register(Pages)
class PagesAdmin(TranslationAdmin):  # Используем TranslationAdmin для поддержки перевода
    list_display = (
        'id',
        'title',
        'category',
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


@admin.register(AdmissionStudents)
class AdmissionStudentsAdmin(TranslationAdmin):  # Используем TranslationAdmin для поддержки перевода
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

admin.site.register(Contact)