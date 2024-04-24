from rest_framework import generics, permissions

from apps.gallery.models import ClassLesson, GalleryImages
from apps.gallery.serializers import ClassLessonSerializer, GallerySerializer


class ClassLessonAPIView(generics.ListAPIView):
    queryset = ClassLesson.objects.all()
    serializer_class = ClassLessonSerializer
    permissions = [permissions.AllowAny]


class GalleryAPIView(generics.ListAPIView):
    queryset = GalleryImages.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = GallerySerializer
