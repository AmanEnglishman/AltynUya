from rest_framework import serializers

from apps.gallery.models import ClassLesson, GalleryImages


class ClassLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLesson
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = '__all__'
