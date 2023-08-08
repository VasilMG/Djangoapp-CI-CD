from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import Q

from ExchangeLogistics.accounts.forms import CreateCompanyProfileForm
from ExchangeLogistics.accounts.models import CompanyProfile
from ExchangeLogistics.common.models import AboutData
from ExchangeLogistics.exchange.forms import CreateOfferForm
from ExchangeLogistics.exchange.models import Offer

UserModel = get_user_model()


class CompanyProfileView(LoginRequiredMixin, generic.DetailView):
    model = CompanyProfile
    template_name = 'exchange/company_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = UserModel.objects.get(pk=self.request.user.pk)
        context['offers'] = Offer.objects.filter(
            company=UserModel.objects.get(pk=self.object.pk)
        ).order_by('-created_on')

        return context


@login_required(login_url='sign_in')
def create_offer(request, pk):
    if request.method == "GET":
        form = CreateOfferForm()
    else:
        form = CreateOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.company = UserModel.objects.get(pk=pk)
            offer.save()
            return HttpResponseRedirect(reverse('offer_details', kwargs={'pk': offer.pk}))
        else:
            return render(request, 'exchange/create_offer.html', {'form': form}, status=404)
    context = {

        'form': form,
    }
    return render(request, 'exchange/create_offer.html', context)


class OfferDetails(LoginRequiredMixin, generic.DetailView):
    model = Offer
    template_name = 'exchange/offer_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = CompanyProfile.objects.get(pk=self.object.company_id)
        if self.request.user.pk == self.object.company_id:
            context['edit'] = 'edit'
            context['delete'] = 'delete'
            context['current_offer'] = self.object
        return context


class ListOffers(LoginRequiredMixin, generic.ListView):
    model = Offer
    template_name = 'exchange/order_list.html'
    paginate_by = 5
    ordering = '-created_on'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        pattern = self.__get_pattern()
        if pattern:
            qs = qs.filter(Q(loading_place__icontains=pattern.lower()) | Q(loading_country__icontains=pattern.lower()))
        return qs

    def __get_pattern(self):
        return self.request.GET.get('pattern', '')


class EditOffer(LoginRequiredMixin, generic.UpdateView):
    model = Offer
    form_class = CreateOfferForm
    template_name = 'exchange/edit-offer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse('offer_details', kwargs={'pk': self.object.pk})


class EditCompanyProfileView(LoginRequiredMixin, generic.UpdateView):
    model = CompanyProfile
    form_class = CreateCompanyProfileForm
    template_name = 'exchange/edit_profile.html'
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
        return render(self.request, 'exchange/edit_profile.html', context, status=404)


class DeleteProfile(LoginRequiredMixin, generic.DeleteView):
    model = CompanyProfile
    success_url = 'index'
    template_name = 'exchange/delete_profile.html'


@login_required(login_url='sign_in')
def confirmation_delete_profile(request, pk):
    if request.method == 'GET':
        offers = Offer.objects.filter(company_id=request.user.pk)
        if offers:
            for offer in offers:
                offer.delete()
        user = UserModel.objects.get(pk=request.user.pk)
        user.delete()
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url='sign_in')
def delete_offer(request, pk):
    if request.method == "GET":
        offer = Offer.objects.get(pk=pk)

        offer.delete()
        return HttpResponseRedirect(reverse('profile_details_company', kwargs={'pk': request.user.pk}))


def support(request):
    context = {
        'support': AboutData.objects.first(),
    }
    return render(request, 'exchange/support.html', context)
