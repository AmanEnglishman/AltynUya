from rest_framework import serializers

from apps.news.models import News, Numbers, Files, Pages


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'


class ContactSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    message = serializers.CharField()
