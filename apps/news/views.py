from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import get_language


from apps.news.models import News, Numbers, Files, Pages
from apps.news.serializers import (NewsSerializer,
                                   NumbersSerializer,
                                   FilesSerializer,
                                   PagesSerializer, ContactSerializer)


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = NewsSerializer


class СontactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilesAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        files = Files.objects.all()
        serializer = FilesSerializer(files, many=True)
        return Response(serializer.data)


class AboutUsItemsAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=1)
        serializer = PagesSerializer(items, many=True)
        return Response(serializer.data)


class VolunteeringListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=3)
        serializer = PagesSerializer(items, many=True)
        return Response(serializer.data)


class OtherSchoolEventsListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=2)
        serializer = PagesSerializer(items, many=True)
        return Response(serializer.data)


class HomePageAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        return News.objects.all().order_by('-created_date')[:4]



class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    