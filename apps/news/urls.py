from django.urls import path

from apps.news import views

urlpatterns = [
    path('', views.HomePageAPIView.as_view(), name='home-page'),
    path('news/', views.NewsListAPIView.as_view(), name='news-list'),
    path('volunteering/', views.VolunteeringListAPIView.as_view(), name='volunteering-list'),
    path('contact-us/', views.ContactAPIView.as_view(), name='contact-us'),
    path('about-us/', views.AboutUsItemsAPIView.as_view(), name='about-us'),
    path('files/', views.FilesAPIView.as_view(), name='files-list'),
    path('news/<int:pk>', views.NewsDetailAPIView.as_view(), name='detail-news'),
    path('other-events/', views.OtherSchoolEventsListAPIView.as_view(), name='other-school-events'),
    path('areas-work/', views.AreasOfWorkListAPIView.as_view(), name='areas-of-work'),
    path('admission/', views.AdmissionStudentsListAPIView.as_view(), name='admission-list')
]