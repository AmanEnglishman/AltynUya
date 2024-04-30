from modeltranslation.translator import translator, TranslationOptions
from apps.teachers.models import Qualification, Teacher, Vacancy, Contingent


class QualificationTranslationOptions(TranslationOptions):
    fields = ('description',)


class TeacherTranslationOptions(TranslationOptions):
    fields = ('job_title',)



class VacancyTranslationOptions(TranslationOptions):
    fields = ('job_title', 'duty', 'requirements', 'conditions')


class ContingentTranslationOptional(TranslationOptions):
    fields = ('text',)


translator.register(Qualification, QualificationTranslationOptions)
translator.register(Teacher, TeacherTranslationOptions)
translator.register(Vacancy, VacancyTranslationOptions)
translator.register(Contingent, ContingentTranslationOptional)