from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import generics as rest_views, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ExchangeLogistics.accounts.api.serializers import CreateUserSerializer, \
    UpdateUserProfileSerializer, LoginUserSerializer
from ExchangeLogistics.accounts.models import CompanyProfile

UserModel = get_user_model()


class CreateUserApiView(rest_views.CreateAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializar = CreateUserSerializer(data=request.data)
        user = get_user_model()
        if not serializar.is_valid():
            return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializar.is_valid():
            try:
                validate_password(serializar.validated_data['password'], user)
            except ValidationError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        user = UserModel.objects.create(
            username=serializar.validated_data['username'],
            password=serializar.validated_data['password'])
        user.set_password(serializar.validated_data['password'])
        user.save()
        the_profile = CompanyProfile.objects.create(user=user)
        the_profile.save()
        serializar.validated_data.pop('confirm_password')
        login(request, user)
        return Response('Created', status=status.HTTP_201_CREATED)


class UpadateUserProfileApiView(rest_views.RetrieveUpdateAPIView):
    serializer_class = UpdateUserProfileSerializer
    queryset = CompanyProfile.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)

        return Response(str(instance), status=status.HTTP_201_CREATED)


class LoginUserApiView(APIView):
    serializer_class = LoginUserSerializer
    queryset = UserModel.objects.all()

    def post(self, request):
        username = self.request.data['username']
        password = self.request.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(str(user), status=status.HTTP_200_OK)
        else:
            return Response('Incorrect username or password', status=status.HTTP_404_NOT_FOUND)
