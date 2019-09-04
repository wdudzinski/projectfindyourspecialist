"""projektx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from projekt1.views import LoginView, LogoutView, HomePageView, SpecialistBoardView, CustomerBoardView,\
    AddCustomerOfferView, AddSpecialistOfferView, AddUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^specialistboard/', SpecialistBoardView.as_view(), name="specialistboard"),
    url(r'^customerboard/', CustomerBoardView.as_view(), name="customerboard"),
    url(r'^addcustomeroffer/', AddCustomerOfferView.as_view(), name="addcustomeroffer"),
    url(r'^addspecialistoffer/', AddSpecialistOfferView.as_view(), name="addspecialistoffer"),
    url(r'^register/', AddUserView.as_view(), name="adduser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
