from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SpecialistOffer, CustomerOffer
from .forms import LoginViewForm, AddCustomerOfferForm, AddSpecialistOfferForm


class HomePageView(View):
    def get(self, request):
        user = request.user
        return render(request, 'home.html', {'user': user})


class LoginView(View):
    def get(self, request):
        form = LoginViewForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginViewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return "Nieprawidłowe dane"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')


class SpecialistBoardView(View):
    def get(self, request):
        specialist_offers = SpecialistOffer.objects.all()
        return render(request, 'specialistboard.html', {'specialist_offers':specialist_offers})


class CustomerBoardView(View):
    def get(self, request):
        customer_offers = CustomerOffer.objects.all()
        return render(request, 'customerboard.html', {'customer_offers':customer_offers})


class AddSpecialistOfferView(View):
    def get(self, request):
        form = AddSpecialistOfferForm()
        return render(request, 'addspecialistoffer.html', {'form': form})

    def post(self, request):
        form = AddSpecialistOfferForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            speciality = form.cleaned_data['speciality']
            description = form.cleaned_data['description']
            priceperhour = form.cleaned_data['priceperhour']
            available_from = form.cleaned_data['available_from']
            available_to = form.cleaned_data['available_to']
            so = SpecialistOffer.objects.create(name=name,
                                                speciality=speciality,
                                                description=description,
                                                priceperhour=priceperhour,
                                                available_from=available_from,
                                                available_to=available_to)
            return HttpResponseRedirect(f"/specialistoffer/{so.id}")
        return render(request, 'addspecialistoffer.html', {'form': form})


class AddCustomerOfferView(View):
    def get(self, request):
        form = AddCustomerOfferForm()
        return render(request, 'addspecialistoffer.html', {'form': form})

    def post(self, request):
        form = AddCustomerOfferForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            speciality = form.cleaned_data['speciality']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            co = SpecialistOffer.objects.create(name=name,
                                                speciality=speciality,
                                                description=description,
                                                price=price)
            return HttpResponseRedirect(f"/customeroffer/{co.id}")
        return render(request, 'addcustomeroffer.html', {'form': form})

