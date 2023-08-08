from django import forms

from ExchangeLogistics.common.models import PrimaryService, SecondaryService, Location, AboutData


class CreatePrimaryServiceModelForm(forms.ModelForm):
    class Meta:
        model = PrimaryService
        fields = '__all__'

    def clean(self):
        main_services= len(PrimaryService.objects.all())
        if main_services == 3:
            raise forms.ValidationError("There must be maximum 3 main services")


class EditPrimaryServiceModelForm(forms.ModelForm):
    class Meta:
        model = PrimaryService
        fields = '__all__'

class CreateEditSecondaryServiceModelForm(forms.ModelForm):
    class Meta:
        model = SecondaryService
        fields = '__all__'

class CreateEditLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class CreateAboutData(forms.ModelForm):
    class Meta:
        model = AboutData
        fields = '__all__'

    def clean(self):
        main_service = AboutData.objects.first()
        if main_service:
            raise forms.ValidationError("There must be only one model of this type")

class EditAboutData(forms.ModelForm):
    class Meta:
        model = AboutData
        fields = '__all__'
