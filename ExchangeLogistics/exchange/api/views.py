from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics as rest_views, status
from rest_framework.response import Response

from ExchangeLogistics.exchange.api.serializers import UserProfileDetailsApiSerializer, CreateOfferSerializer, \
    CompleteOfferDetailsSerializer, ShortOfferSerializer
from ExchangeLogistics.exchange.models import Offer

UserModel = get_user_model()


class ProfileDetailsApiView(LoginRequiredMixin, rest_views.RetrieveAPIView):
    serializer_class = UserProfileDetailsApiSerializer
    queryset = UserModel.objects.all()


class ViewDetailsDeleteUserProfileApiView(LoginRequiredMixin, rest_views.RetrieveDestroyAPIView):
    serializer_class = UserProfileDetailsApiSerializer
    queryset = UserModel.objects.all()


class CreateOfferApiView(LoginRequiredMixin, rest_views.CreateAPIView):
    serializer_class = CreateOfferSerializer
    queryset = Offer.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = UserModel.objects.get(pk=kwargs.get('pk'))
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        offer = serializer.save()
        offer.company = user
        offer.save()

        return Response('Created', status=status.HTTP_201_CREATED)


class UpdateOfferApiView(LoginRequiredMixin, rest_views.RetrieveUpdateAPIView):
    serializer_class = CreateOfferSerializer
    queryset = Offer.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)

        return Response(str(instance), status=status.HTTP_201_CREATED)


class DeleteOfferApiView(LoginRequiredMixin, rest_views.RetrieveDestroyAPIView):
    serializer_class = CompleteOfferDetailsSerializer
    queryset = Offer.objects.all()


class ListOffersApiView(LoginRequiredMixin, rest_views.ListAPIView):
    serializer_class = ShortOfferSerializer
    queryset = Offer.objects.all().order_by('-created_on')
