def login(request):
    data = {'pass': "unsucessful ",
            'privateAddress': "unsucessful",
            'account_number': "unsucessful",
            'status': "undefined",
            }
    template_name = 'TradeSite/login.html'
    if request.method == 'POST':
        password = request.POST['pwd']

        ####################################
        privateAddress = request.POST['addr']
        if alreadyExists(password) and UserAccount.objects.filter(password=password).exists():
            if getAccountNumber(password):
                request.session['user_account'] = getAccountNumber(password)
                request.session['status'] = "Pass"
            ##
            else:
                request.session['status'] = "Error Login : Invalid Credentials"
        else:
            request.session['status'] = "Error Login: Account does not Exist"
        ##validation
        ##################################

        data = {
            'pass': password,
            'privateAddress': privateAddress,
            'account_number': request.session['user_account'],
            'status': request.session['status'],

        }

    return render(request, template_name, data)















<form action="{% url 'TradeSite:login' %}" method="POST" >
    {% csrf_token %}
<div class="container-fluid col-lg-offset-3">
  <div class="col-sm-8" >
    <p>Enter your wallet address</p> <input type="password" class="form-control " name="addr"><br />
    <p>Enter your password</p><input type="password" class="form-control " name="pwd">
  </div></div>
    <br />
    <input type="submit" name="send" class="btn btn-primary btn-lg center-block" value="Securely Log In">
</form>


