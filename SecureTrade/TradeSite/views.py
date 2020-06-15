import datetime
import base64
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.views import generic
from django.utils import timezone
from django_tables2 import tables

from .tables import CustomTable
from . import AES
from . import config
from .queryOfSolidity import Queries
from .ethereum_account import CreateAccount
from .querySetOfDjano import alreadyExists, getAccountNumber
from .models import UserAccount, TransactionHistory
from .forms import RegistForm, LoginForm


class IndexView(generic.ListView):

    def normaIndex(request):
        form = LoginForm()
        data = {
            'pass': "unsucessful ",
                'privateAddress': "unsucessful",
                'account_number': "unsucessful",
                'status': "undefined",
                'form' : form
                }

        if request.method =='POST':
            password = request.POST.get('q', None)
         ####################
        form = LoginForm(request.POST)
        if form.is_valid():
            private_key = form.cleaned_data['key']
            password = form.cleaned_data['password']


            template_name = 'TradeSite/index.html'
            if request.method == 'POST':
                privateAddress = private_key
                if alreadyExists(password) and UserAccount.objects.filter(password=password).exists():
                    if getAccountNumber(password):
                        request.session['user_account'] = getAccountNumber(password)
                        request.session['private_key'] = Queries.getPrivateKeyText(privateAddress)
                        request.session['status'] = "Pass"
                    ##
                    else:
                        request.session['status'] = "Error Login : Invalid Credentials"
                else:
                    request.session['status'] = "Error Login: Account does not Exist"
                ##validation
                ##################################

                data = {
                    'form' : form,
                    'pass': password,
                    'privateAddress': privateAddress,
                    'account_number': request.session['user_account'],
                    'status': request.session['status'],
                }


        ########################
        try :
            template_name = 'TradeSite/index.html'
            if request.session['user_account'] :
                data = {
                        'user_account': request.session['user_account'],
                        'form': form,
                 }
                return render(request, template_name, data)
            else :
                return render(request, 'TradeSite/login.html', data)

        except KeyError:
            pass
            return render(request, 'TradeSite/login.html', data)


    def get_queryset(self):
        """Return the last five published questions."""
        return ("")



class WalletView(generic.ListView):
    def wallet(request):
        text="Not Approved!!"
        if request.POST.get('Send') == 'Send':
            amount = request.POST.get('amount')
            fromAddr = request.session['user_account']
            toAddr = request.POST.get('addr')
            tx = Queries.approve(fromAddr, amount, request.session['private_key'])
            Queries.transferCustom(request.session['private_key'], toAddr, amount)
            # Queries.transferFrom(fromAddr,toAddr,amount, request.session['private_key'])
                #########################
            #sending to sql db
            q = TransactionHistory(sender=fromAddr, receiver=toAddr, transaction_date=timezone.now(), amount=amount)
            q.save()

            ###################################
        template_name = 'TradeSite/wallet.html'



        if request.POST.get('approve') == 'approve':
            amount = request.POST.get('amount')
            address = request.session['user_account']
            tx = Queries.approve(address, amount, request.session['private_key'])
            text = "approved"
        template_name = 'TradeSite/wallet.html'
        data = {'addr': request.session['user_account'],
                'bal': Queries.getAccountBalance(request.session['user_account']),
                'text': text
                }
        return render(request, template_name, data)


class BuyView(generic.ListView):
    def buy(request):
        if request.POST.get('Send') == 'Buy':
            amount = request.POST.get('amount')
            address = request.POST.get('addr')
            Queries.transfer(address, amount)
        template_name = 'TradeSite/buy.html'
        data = {
            'addr' : request.session['user_account'],
            'bal' : Queries.getAccountBalance(request.session['user_account']),
        }
        return render(request, template_name, data)



    def buy_items(request):
        item_addr="adasd"
        item_id=""
        item_price=""

        if request.POST.get('Send') == 'Buy':
            amount = request.POST.get('amount')
            address = request.POST.get('addr')
            Queries.transfer(address, amount)


        item_id =  str(base64.b64decode(request.GET.get('item_id')), "utf-8")
        item_price =  str(base64.b64decode(request.GET.get('price')), "utf-8")
        item_addr =  str(base64.b64decode(request.GET.get('seller_addr')), "utf-8")
        template_name = 'TradeSite/buy_items.html'
        data = {
            'addr': request.session['user_account'],
            'bal': Queries.getAccountBalance(request.session['user_account']),
            'url_item_price': item_price,
            'url_item_addr': item_addr,
            'url_item_id': item_id,
        }
        if request.POST.get('btnConfirm') == 'Confirm':
            tx = Queries.approve(item_addr, item_price, request.session['private_key'])
            # Queries.transfer(item_addr, item_price)
            Queries.transferCustom(request.session['private_key'], item_addr, item_price)
            q = TransactionHistory(sender=request.session['private_key'], receiver=item_addr, transaction_date=timezone.now(), amount=item_price)
            q.save()
            return render(request, template_name, data)


        return render(request, template_name, data)


class LoginView(generic.ListView):
    def login(request):
        if 'user_account' in request.session:
            return render(request, 'TradeSite/index.html',)

        form = LoginForm(request.POST)
        return render(request, 'TradeSite/login.html', {'form': form})


def register(request):
        form = RegistForm(request.POST)
        return render(request, 'TradeSite/register.html', {'form':form} )

class TransactionView(tables.Table):
    class Meta:
        model = TransactionHistory
        template_name = 'django_tables2/bootstrap4.html'

    def transactions(request):
        template_name = 'TradeSite/transactions.html'
        queryset = TransactionHistory.objects.all()
        table = TransactionView(queryset)
        return render(request, template_name,{'transactions_data':table} )

def logout(request):
        try:
            form = RegistForm()
            del request.session['user_account']
            del request.session['private_key']
            del request.session['status']
            return render(request, 'TradeSite/login.html', {'form': form})
        except KeyError:
            form = RegistForm()
            return HttpResponseRedirect('/login')






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
                    request.session['user_account'] = accountNumber
                    request.session['private_key'] = Queries.getPrivateKeyText(private_key)
                    args = {'form': form, 'password': password, 'data': "account Created", 'account_address':accountNumber, 'private_key':request.session['private_key']}
                    return render(request, template_name, args)

        else:
            template_name = 'TradeSite/afterRegist.html'
            form = RegistForm()
            password = form.cleaned_data['post']
            return render(request, template_name, {'form': form, 'password': password})

