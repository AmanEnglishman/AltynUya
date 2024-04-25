from modeltranslation.translator import translator, TranslationOptions
from apps.news.models import News, Category, Pages, AdmissionStudents


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class AdmissionStudentsTransaltionOptions(TranslationOptions):
    fields = ('title_head', 'text_head', 'title', 'text')


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Pages, PagesTranslationOptions)
translator.register(AdmissionStudents, AdmissionStudentsTransaltionOptions)