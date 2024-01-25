from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, ChangePasswordSerializer

User = get_user_model()
class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomSignupView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            username = request.data.get('username')
            token = Token.objects.get(user=user)
            data = {
                'username': username,
                'token': token.key
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST', 'PUT'])
    def change_password(self, request):
        user = self.request.user
        serializer = ChangePasswordSerializer(user, request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'mess': 'password changed'}, status=status.HTTP_200_OK)
        return Response({'mess': 'error'}, status=status.HTTP_400_BAD_REQUEST)