from django.urls import path

from .views import TeacherListView, QualificationListView, VacancyListView, ContingentListView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('qualifications/', QualificationListView.as_view(), name='qualification-list'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('contingent/', ContingentListView.as_view(), name='contingent-list'),

]