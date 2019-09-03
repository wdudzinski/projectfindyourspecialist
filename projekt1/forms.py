from django import forms
from .models import SpecialistOffer, CustomerOffer


class AddSpecialistOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialistOffer
        fields = ('name', 'speciality', 'description', 'priceperhour', 'available_from', 'available_to')


class AddCustomerOfferForm(forms.ModelForm):
    class Meta:
        model = CustomerOffer
        fields = ('name', 'speciality', 'description', 'price')


class LoginViewForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)