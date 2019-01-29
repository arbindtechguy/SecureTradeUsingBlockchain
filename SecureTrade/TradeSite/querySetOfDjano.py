from .models import UserAccount

def getAllUserAccount():
    query = UserAccount.object.all()

def alreadyExists(password):
    if UserAccount.objects.filter(password=password).exists():
        return True
    else :
        return False

