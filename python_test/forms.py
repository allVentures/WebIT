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
