from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.models import User
from apps.user.permissions import AnonPermission
from apps.user.serializers import MyTokenSerializer, UserSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer


class UserRegisterView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
