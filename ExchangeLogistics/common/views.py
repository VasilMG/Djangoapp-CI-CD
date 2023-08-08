from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect


from ExchangeLogistics.common.forms import CreatePrimaryServiceModelForm, EditPrimaryServiceModelForm, \
    CreateEditSecondaryServiceModelForm, CreateEditLocation, CreateAboutData, EditAboutData
from ExchangeLogistics.common.models import PrimaryService, SecondaryService, Location, AboutData


def index(request):
    primary_services = PrimaryService.objects.all()
    secondary_services = SecondaryService.objects.all()
    context = {
        'primary_services': primary_services,
        'secondary_services': secondary_services,
    }
    return render(request, 'common/index.html', context)


def services(request):
    primary_services = PrimaryService.objects.all()
    secondary_services = SecondaryService.objects.all()
    context = {
        'primary_services': primary_services,
        'secondary_services': secondary_services,
    }
    return render(request, 'common/services_main.html', context)


def network(request):
    offices = Location.objects.all().order_by('country')
    context = {
        'offices': offices,
    }
    return render(request, 'common/network.html', context)


def about(request):
    data = AboutData.objects.first()
    context = {
        'data': data,
    }
    return render(request, 'common/about.html', context)

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def settings_view(request):
    return render(request, 'common/settings.html')

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def primary_services_view(request):
    context = {
        'objects': PrimaryService.objects.all(),
    }
    return render(request, 'common/list-primary.html', context=context)

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def create_primary_service_view(request):
    if request.method == 'GET':
        form = CreatePrimaryServiceModelForm()
    else:
        form = CreatePrimaryServiceModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('primary_services')
    return render(request, 'common/create-primary.html', context={'form': form,})

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_primary_view(request, pk):
    current_service = PrimaryService.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditPrimaryServiceModelForm(instance=current_service)
    else:
        form = EditPrimaryServiceModelForm(request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()
            return redirect('primary_services')
    return render(request, 'common/edit-primary.html', context={'form': form, 'service': current_service, })

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_primary_view(request, pk):
    current_model = PrimaryService.objects.get(pk=pk)
    current_model.delete()
    return redirect('primary_services')

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def secondary_services_view(request):
    context = {
        'objects': SecondaryService.objects.all(),
    }
    return render(request, 'common/list-secondary.html', context=context)


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def create_secondary_service_view(request):
    if request.method == 'GET':
        form = CreateEditSecondaryServiceModelForm()
    else:
        form = CreateEditSecondaryServiceModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('secondary_services')
    return render(request, 'common/create-secondary.html', context={'form': form,})


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_secondary_view(request, pk):
    current_service = SecondaryService.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreateEditSecondaryServiceModelForm(instance=current_service)
    else:
        form = CreateEditSecondaryServiceModelForm(request.POST, request.FILES, instance=current_service)
        if form.is_valid():
            form.save()
            return redirect('secondary_services')
    return render(request, 'common/edit-secondary.html', context={'form': form, 'service': current_service, })


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_secondary_view(request, pk):
    current_model = SecondaryService.objects.get(pk=pk)
    current_model.delete()
    return redirect('secondary_services')


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def locations_view(request):
    context = {
        'objects': Location.objects.all(),
    }
    return render(request, 'common/list-locations.html', context=context)


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def create_location_view(request):
    if request.method == 'GET':
        form = CreateEditLocation()
    else:
        form = CreateEditLocation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations')
    return render(request, 'common/create-location.html', context={'form': form, })


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_location_view(request, pk):
    location = Location.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreateEditLocation(instance=location)
    else:
        form = CreateEditLocation(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('locations')
    return render(request, 'common/edit-location.html', context={'form': form, 'service': location, })


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_location_view(request, pk):
    current_model = Location.objects.get(pk=pk)
    current_model.delete()
    return redirect('locations')

@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def about_data_view(request):
    context = {
        'objects': AboutData.objects.all(),
    }
    return render(request, 'common/list-about.html', context=context)


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def create_about_view(request):
    if request.method == 'GET':
        form = CreateAboutData()
    else:
        form = CreateAboutData(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_data')
    return render(request, 'common/create-about.html', context={'form': form, })


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_about_view(request, pk):
    about_data = AboutData.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditAboutData(instance=about_data)
    else:
        form = EditAboutData(request.POST, instance=about_data)
        if form.is_valid():
            form.save()
            return redirect('about_data')
    return render(request, 'common/edit-about.html', context={'form': form, 'service': about_data, })


@login_required(login_url='sign_in')
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_about_view(request, pk):
    current_model = AboutData.objects.get(pk=pk)
    current_model.delete()
    return redirect('about_data')

