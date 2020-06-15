"""SecureTrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, re_path

from . import views
app_name = 'TradeSite'

urlpatterns = [
    path(r'index/', views.IndexView.normaIndex, name='index'),
    path(r'login/', views.LoginView.login, name='login'),
    path(r'wallet/', views.WalletView.wallet, name='wallet'),
    path(r'transactions/', views.TransactionView.transactions, name='transactions'),
    path(r'buy/', views.BuyView.buy, name='buy'),
    path(r'buy_items/', views.BuyView.buy_items, name='buy_items'),
    path(r'register/', views.register, name='register'),
    path(r'logout/', views.logout, name='logout'),
    path(r'afterRegist/', views.AfterRegisterView.afterRegister, name='afterRegist'),

]
