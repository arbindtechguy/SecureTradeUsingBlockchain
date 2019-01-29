from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract
w3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/032b2cbaaefc4ad5b7fc1a875fbed094", websocket_kwargs={'timeout': 60}))
from eth_account import Account

class CreateAccount:
    def getNewAccount(password):
        newAccount = Account.create(password)
        return newAccount

    def getAccountAddress(accountObj):
        account_address = accountObj.address
        return account_address

    def getAccountPrivateKey(accountObj):
        private_key = accountObj.privateKey
        return private_key

    def getAccountObjectByPrivateKey(key):
        acc = Account.privateKeyToAccount(key)
        return acc


# new_account = getNewAccount("arbind")
# acc_addr = getAccountAddress(new_account)
# print('Account addreess:',acc_addr)
# private_key = getAccountPrivateKey(new_account)
# print("Private Key:", private_key)
# acc_addr = getAccountAddress(getAccountObjectByPrivateKey(private_key))
# print("Account Address:", acc_addr)
