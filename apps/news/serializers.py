from rest_framework import serializers

from apps.news.models import News, Numbers, Files, Pages, AdmissionStudents, Contact


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
    image = serializers.SerializerMethodField()

    class Meta:
        model = Pages
        fields = ('title', 'title_ru', 'title_ky', 'author', 'text', 'text_ru', 'text_ky', 'created_date', 'image', 'category')

    def get_image(self, obj):
        if obj.image:  # Проверяем, что поле изображения не пустое
            return self.context['request'].build_absolute_uri(obj.image.url)
        else:
            return None
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'message']



class AdmissionStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionStudents
        fields = '__all__'
