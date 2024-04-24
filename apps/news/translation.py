from modeltranslation.translator import translator, TranslationOptions
from apps.news.models import News, Category, Pages


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)



class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Pages, CategoryTranslationOptions)