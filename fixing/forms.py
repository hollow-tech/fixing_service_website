from phonenumber_field.formfields import PhoneNumberField
from .models import Worker, Order
from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label="Имя", max_length="50")
    phone_number = PhoneNumberField(label="Телефон")
    workers = forms.ModelChoiceField(
        queryset=Worker.objects.all(), label="Что нужно починить?", widget=forms.Select(), empty_label=None
    )



class ConsultationForm(forms.Form):
    name = forms.CharField(label="Имя", max_length="50")
    phone_number = PhoneNumberField(label="Телефон")
    workers = forms.ModelChoiceField(
        queryset=Worker.objects.all(), label="Что нужно починить?", widget=forms.Select(), empty_label=None
    )
