from django.urls import path

from apps.news import views

urlpatterns = [
    path('', views.HomePageAPIView.as_view(), name='home-page'),
    path('news/', views.NewsListAPIView.as_view(), name='news-list'),
    path('volunteering/', views.VolunteeringListAPIView.as_view(), name='for-parents-list'),
    path('contact-us/', views.СontactAPIView.as_view(), name='contact-us'),
    path('about-us/', views.AboutUsItemsAPIView.as_view(), name='about-us'),
    path('files/', views.FilesAPIView.as_view(), name='files-list'),
    path('news/<int:pk>', views.NewsDetailAPIView.as_view(), name='detail-news')
]