from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SpecialistOffer, CustomerOffer
from .forms import LoginViewForm, AddCustomerOfferForm, AddSpecialistOfferForm, AddUserForm


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
            speciality = form.cleaned_data['speciality']
            description = form.cleaned_data['description']
            priceperhour = form.cleaned_data['priceperhour']
            available_from = form.cleaned_data['available_from']
            so = SpecialistOffer.objects.create(speciality=speciality,
                                                description=description,
                                                priceperhour=priceperhour,
                                                available_from=available_from)
            return HttpResponseRedirect(f"/specialistoffer/{so.id}")
        return render(request, 'addspecialistoffer.html', {'form': form})


class AddCustomerOfferView(View):
    def get(self, request):
        form = AddCustomerOfferForm()
        return render(request, 'addspecialistoffer.html', {'form': form})

    def post(self, request):
        form = AddCustomerOfferForm(request.POST)
        if form.is_valid():
            speciality = form.cleaned_data['speciality']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            co = CustomerOffer.objects.create(speciality=speciality,
                                              description=description,
                                              price=price)
            return HttpResponseRedirect(f"/customeroffer/{co.id}")
        return render(request, 'addcustomeroffer.html', {'form': form})


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'adduser.html', {'form':form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            passwordconfirm = form.cleaned_data.get('passwordconfirm')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            if password == passwordconfirm:
                u=User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
                u.set_password(password)
                u.save()
                return HttpResponseRedirect('/login')
            else:
                return HttpResponse("Nieprawidłowe dane!")


