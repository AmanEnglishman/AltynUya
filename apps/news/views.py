from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import get_language


from apps.news.models import News, Numbers, Files, Pages, AdmissionStudents
from apps.news.serializers import (NewsSerializer,
                                   NumbersSerializer,
                                   FilesSerializer,
                                   PagesSerializer, 
                                   ContactSerializer,
                                   AdmissionStudentsSerializer)


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_date')
    permission_classes = [permissions.AllowAny]
    serializer_class = NewsSerializer


class ContactAPIView(APIView):
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
        files = Files.objects.all().order_by('-id')
        serializer = FilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            file_id = request.data.get('id')
            file_instance = Files.objects.get(id=file_id)
            file_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Files.DoesNotExist:
            return Response({"error": "File does not exist."}, status=status.HTTP_404_NOT_FOUND)


class AboutUsItemsAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=1)
        serializer = PagesSerializer(items, many=True,  context={'request': request})
        return Response(serializer.data)


class VolunteeringListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=3).order_by('-id')
        serializer = PagesSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)


class OtherSchoolEventsListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=2).order_by('-id')
        serializer = PagesSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)
    
class AreasOfWorkListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=4).order_by('-id')
        serializer = PagesSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)

class PartnershipListAPIView(APIView):
    def get(self, request):
        items = Pages.objects.filter(category_id=5).order_by('-id')
        serializer = PagesSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)


class HomePageAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        return News.objects.all().order_by('-created_date')[:4]



class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    


class AdmissionStudentsListAPIView(generics.ListAPIView):
    queryset = AdmissionStudents.objects.all()
    serializer_class = AdmissionStudentsSerializer
    permission_classes = [permissions.AllowAny]