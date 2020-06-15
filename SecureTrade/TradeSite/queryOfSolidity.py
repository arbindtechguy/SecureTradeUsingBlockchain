import time
from .models import UserAccount
from web3 import Web3
from eth_account import Account
from . import config
class Queries :
    w3 = config.conf.w3
    MyC_contract = config.conf.MyC_contract

    def checkAccountExists(key):
        try :
            private_key = Account.privateKeyToAccount(key)
            return True
        except:
            return False

    def getAccountFromKey(key):
        try :
            private_key = Account.privateKeyToAccount(key)
            return private_key
        except:
            return False

    def getPrivateKeyText(key):
        try:
            obj = Account.privateKeyToAccount(key)
            return obj.privateKey.hex()
        except:
            return False


    def getAccountBalance(address):
        try:
            balance = Queries.MyC_contract.functions.balanceOf(address).call()
            return balance
        except:
            return False


    def transfer(address, amoun):
        account_obj = config.conf.account_obj
        txn = Queries.MyC_contract.functions.transfer(address, int(amoun)).buildTransaction({
            'from': account_obj.address,
            'nonce': Queries.w3.eth.getTransactionCount(account_obj.address),
            'gas': 1728712,
            'gasPrice': Queries.w3.toWei('21', 'gwei')}
        )

        signed = account_obj.signTransaction(txn)
        tx_hash = Queries.w3.eth.sendRawTransaction(signed.rawTransaction)
        config.conf.wait_for_receipt(Queries.w3, tx_hash, 1)


    def approve(spender_address, amount, key):
        account_obj = Account.privateKeyToAccount(key)
        txn = Queries.MyC_contract.functions.approve(spender_address, int(amount)).buildTransaction({
            'nonce': Queries.w3.eth.getTransactionCount(account_obj.address),
            'gas': 1728712,
            'gasPrice': Queries.w3.toWei('21', 'gwei')}
        )
        signed = account_obj.signTransaction(txn)
        tx_hash = Queries.w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_receipt = config.conf.wait_for_receipt(Queries.w3, tx_hash, 1)
        return tx_receipt


    def transferFrom(fromAddr , toAddr, amount, key):
        w3 = config.conf.w3
        account_obj = Account.privateKeyToAccount(key)
        txn = Queries.MyC_contract.functions.transferFrom(fromAddr,w3.toChecksumAddress(toAddr), int(amount)).buildTransaction({
            'nonce': Queries.w3.eth.getTransactionCount(account_obj.address),
            'gas': 1728712,
            'gasPrice': Queries.w3.toWei('21', 'gwei')}
        )

        signed = account_obj.signTransaction(txn)
        tx_hash = Queries.w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_receipt = config.conf.wait_for_receipt(Queries.w3, tx_hash, 1)
        return tx_receipt


    def transferCustom(private_key, address, amoun):
        account_obj = config.conf.getAccountFromPrivateKey(private_key)
        txn = Queries.MyC_contract.functions.transfer(address, int(amoun)).buildTransaction({
            'from': account_obj.address,
            'nonce': Queries.w3.eth.getTransactionCount(account_obj.address),
            'gas': 1728712,
            'gasPrice': Queries.w3.toWei('21', 'gwei')}
        )

        signed = account_obj.signTransaction(txn)
        tx_hash = Queries.w3.eth.sendRawTransaction(signed.rawTransaction)
        config.conf.wait_for_receipt(Queries.w3, tx_hash, 1)