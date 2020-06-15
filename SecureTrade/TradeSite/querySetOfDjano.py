from .models import UserAccount

def getAllUserAccount():
    query = UserAccount.object.all()


def alreadyExists(password):
    if UserAccount.objects.filter(password=password).exists():
        return True
    else :
        return False


def getAccountNumber(password):
    try :
        obj = UserAccount.objects.filter(password=password)
        for i in range(len(obj)):
            return obj[i].account_number

    except:
        return False
