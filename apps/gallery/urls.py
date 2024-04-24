from django.urls import path

from .views import ClassLessonAPIView, GalleryAPIView

urlpatterns = [
    path('gallery/', GalleryAPIView.as_view(), name='gallery'),
    path('lessons/', ClassLessonAPIView.as_view(), name='lessons'),
]
