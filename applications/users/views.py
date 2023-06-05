from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework import status
from django.contrib.auth import get_user_model


from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer


User = get_user_model()


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Thanks for registration!'})
    

class ActivationView(CreateAPIView):
    serializer_class = ActivationSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response({'message': 'Аккаунт успешно активирован!'})


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request) -> Response:
        Token.objects.get(user=request.user).delete()
        return Response({'message': 'Logged out'})
    

# RESET PASSWORD

class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Пароль успешно изменен :)',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# TODO: восстановление пароля: DONE
# TODO: изменение пароля: DONE
