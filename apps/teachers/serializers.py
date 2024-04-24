from rest_framework import serializers

from apps.teachers.models import Teacher, Vacancy, Qualification, Contingent


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'


class ContingentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contingent
        fields = '__all__'
