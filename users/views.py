from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserAuthorizeSerializer, UserCreatSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class AuthorizationAPIView(APIView):
    def post(self, request):
        """ Validate Data """
        serializer = UserAuthorizeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        """ Authenticate (Search) User"""
        user = authenticate(**serializer.validated_data)
        if user:
            """ Authorize User """
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        """ Error on Authorizing"""
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationAPIView(APIView):
    def post(self, request):
        """ Validate Data """
        serializer = UserCreatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        """ Create User """
        user = User.objects.create_user(**serializer.validated_data)
        return Response(data={'user_id': user.id})


def authorization_api_view(request):
    if request.method == 'POST':
        """ Validate Data """
    serializer = UserAuthorizeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=serializer.errors)
    # """ Read Data """
    # username = serializer.validated_data.get("username") get() данные получаются по ключу.
    # password = serializer.validated_data.get("password")
    """ Authenticate (Search) User"""
    # user = authenticate(username=username, password=password)
    user = authenticate(**serializer.validated_data) # username=admin, password=123
                                                     # данные распаковывываются и проверяются
    if user:
        """ Authorize User """
        token, created = Token.objects.get_or_create(user=user) # Если User авторизован то Токен
                                                                # выдается, a если нет то создается
        return Response(data={'key': token.key})
    """ Error on Authorizing"""
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['Post'])
def registration_api_view(request):
    """ Validate Data """
    serializer = UserCreatSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    """ Create User """
    user = User.objects.create_user(**serializer.validated_data)
    return Response(data={'user_id': user.id})