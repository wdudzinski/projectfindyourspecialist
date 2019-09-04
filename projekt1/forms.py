from django import forms
from .models import SpecialistOffer, CustomerOffer


class DateInput(forms.DateInput):
    input_type = 'date'


class AddSpecialistOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialistOffer
        fields = ('speciality', 'description', 'priceperhour', 'available_from')
        widgets = {
            'available_from': DateInput()
        }


class AddCustomerOfferForm(forms.ModelForm):
    class Meta:
        model = CustomerOffer
        fields = ('speciality', 'description', 'price')


class LoginViewForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    passwordconfirm = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    first_name = forms.CharField(label='First name', max_length=128)
    last_name = forms.CharField(label='Last name', max_length=128)
    email = forms.EmailField(label='email')

