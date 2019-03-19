from django import forms
from django.forms.models import ModelForm

from python_test.models import Client


class AddClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('client_name',)

    client_name = forms.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SearchClientForm(forms.Form):
    SORTING = (
        (1, "Client Name"),
        (2, "Suburb"),
        (3, "Email"),
        (4, "Phone")
    )
    ORDER = (
        (1, "ASC"),
        (2, "DSC"),
    )

    client_name = forms.CharField(max_length=128, required=False,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=24, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    suburb = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    sorting = forms.ChoiceField(choices=SORTING)
    order = forms.CharField(widget=forms.RadioSelect(choices=ORDER, attrs={"class": "form-check-input"}), initial=1)
