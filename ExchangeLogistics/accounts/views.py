from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

from ExchangeLogistics.accounts.forms import CreateCompanyAccountForm, CreateCompanyProfileForm
from ExchangeLogistics.accounts.models import CompanyProfile
from ExchangeLogistics.exchange.models import Offer

UserModel = get_user_model()


class CreateCustomUserView(generic.CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = CreateCompanyAccountForm
    success_url = reverse_lazy('create_main_profile')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result

    def get_success_url(self):
        created_object = self.object
        return reverse('create_main_profile', kwargs={'pk': created_object.pk, })

    def form_invalid(self, form):
        context = {
            'form': form,
        }
        return render(self.request, 'accounts/sign-up.html', context)


class UpdateCompanyProfileView(LoginRequiredMixin, generic.UpdateView):
    model = CompanyProfile
    form_class = CreateCompanyProfileForm
    template_name = 'accounts/sign_up_profile.html'
    success_url = reverse_lazy('profile_details_company')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = UserModel.objects.get(pk=self.object.pk)

        return context

    def get_success_url(self):
        return reverse('profile_details_company', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        context = {
            'form': form,
        }
        return render(self.request, 'accounts/sign_up_profile.html', context)


def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm(request)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser or user.is_staff:
                try:
                    the_profile = CompanyProfile.objects.get(user=user)
                except ObjectDoesNotExist:
                    the_profile = CompanyProfile.objects.create(user=user,)
            else:
                the_profile = CompanyProfile.objects.get(user=user)
            login(request, user)
            return HttpResponseRedirect(reverse('profile_details_company', kwargs={'pk': the_profile.pk}))
        else:
            form.error_messages[
                "invalid_login"] = 'Please enter a correct username and password. ' \
                                   'Note that both fields may be case-sensitive.'
            error_message = form.error_messages["invalid_login"]
            return render(request, 'accounts/sign-in.html', {'form': form, 'message': error_message, }, status=404)
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign-in.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect(reverse('index'))
