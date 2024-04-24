from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.teachers.models import Teacher, Vacancy, Qualification, Contingent


@admin.register(Teacher)
class TeachersAdmin(TranslationAdmin):
    list_display = (
        'id',
        'name',
        'surname',
    )
    list_display_links = (
        'id',
        'name',
        'surname',
    )
    list_filter = (
        'id',
        'name',
        'surname',
    )
    search_fields = (
        'id',
        'name',
        'surname',
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


@admin.register(Vacancy)
class VacancyAdmin(TranslationAdmin):
    list_display = (
        'id',
        'job_title',
    )
    list_display_links = (
        'id',
        'job_title',
    )
    list_filter = (
        'id',
        'job_title',
    )
    search_fields = (
        'id',
        'job_title',
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

@admin.register(Qualification)
class QualificationAdmin(TranslationAdmin):
    list_display = (
        'id',
        'teacher',
        'description',
    )
    list_display_links = (
        'id',
        'teacher',
    )
    list_filter = (
        'id',
        'teacher',
    )
    search_fields = (
        'id',
        'teacher',
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


@admin.register(Contingent)
class ContingentAdmin(TranslationAdmin):
    list_display = (
        'id',
        'name',
        'surname'
    )
    list_display_links = (
        'id',
        'name',
        'surname'

    )
    list_filter = (
        'id',
        'name',
        'surname'

    )
    search_fields = (
        'id',
        'name',
        'surname'
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
