from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import HTMLFormRenderer

from .models import Vacancy, Qualification, Teacher, Contingent
from .serializers import VacancySerializer, QualificationSerializer, TeacherSerializer, ContingentSerializer


class VacancyListView(ListAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    permission_classes = (AllowAny,)


class QualificationListView(ListAPIView):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()
    permission_classes = (AllowAny,)


class TeacherListView(ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = (AllowAny,)


class ContingentListView(ListAPIView):
    serializer_class = ContingentSerializer
    queryset = Contingent.objects.all()
    permission_classes = (AllowAny,)
