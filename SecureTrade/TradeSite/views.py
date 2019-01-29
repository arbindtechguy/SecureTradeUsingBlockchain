from django.forms.widgets import Input
from django.shortcuts import render
from django.template import loader, RequestContext
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .ethereum_account import CreateAccount
from .querySetOfDjano import alreadyExists
from .models import UserAccount
from . forms import RegistForm


class IndexView(generic.ListView):
    template_name = 'TradeSite/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ("")

class WalletView(generic.ListView):
    template_name = 'TradeSite/wallet.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ({'name':"Arbind Saraf"})

class LoginView(generic.ListView):
    template_name = 'TradeSite/login.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return ("")



def register(request):
        form = RegistForm(request.POST)
        return render(request, 'TradeSite/register.html', {'form':form} )


class AfterRegisterView(generic.ListView):
    template_name = 'TradeSite/afterRegist.html'

    def afterRegister(request):
        """Return the last five published questions."""
        if (request.method == 'POST'):
            template_name = 'TradeSite/afterRegist.html'
            form = RegistForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['post']
                newAccount = CreateAccount.getNewAccount(password)
                accountNumber = CreateAccount.getAccountAddress(newAccount)
                if alreadyExists(password):
                    return render(request, template_name,{'form': form, 'password': password, 'data': "Account already Created!!"})
                else:
                    private_key = CreateAccount.getAccountPrivateKey(newAccount)
                    data = UserAccount(password=password, account_number=accountNumber)
                    data.save()
                    args = {'form': form, 'password': password, 'data': "account Created", 'account_address':accountNumber, 'private_key':private_key}
                    return render(request, template_name, args)

        else:
            template_name = 'TradeSite/afterRegist.html'
            form = RegistForm()
            password = form.cleaned_data['post']
            return render(request, template_name, {'form': form, 'password': password})

