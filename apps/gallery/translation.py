from modeltranslation.translator import translator, TranslationOptions
from .models import ClassLesson


class CLassLessonTranslationOptions(TranslationOptions):
    fields = ('title', 'title_head', 'text')


translator.register(ClassLesson, CLassLessonTranslationOptions)