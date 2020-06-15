import json
import time
import os
from eth_account import Account
from web3 import Web3
w3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/032b2cbaaefc4ad5b7fc1a875fbed094", websocket_kwargs={'timeout': 60}))
acc = "0x841B02Fe7951B0F14EAa8329f0F62a32EEEc6283"
w3.eth.defaultAccount = acc
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
with open(os.path.join(PROJECT_ROOT, "abi.py")) as f:
    info_json = json.load(f)
abi =  info_json

contract_address = "0x49b6e5581bf10a301b4fcc9d5fcf4662c9231c13"
MyC_contract = w3.eth.contract(address= w3.toChecksumAddress(contract_address), abi=abi)

account_obj = Account.privateKeyToAccount(b"c\x15\x19\xc8\xc1\xf3GV\x07[65\xf8\x89Ul\xa8\x9e$\xff\xf6;\xdeK\x14'\x81;g\xc6\xa2\xcd")

print('Total Supply: {}'.format(
    MyC_contract.functions.totalSupply().call()
))
print('Balance of "Original" : {}'.format(
    MyC_contract.functions.balanceOf(account_obj.address).call()
))

txn = MyC_contract.functions.transfer("0xb63767ce5946b3C5a2F849854DF24B2401328168",20000).buildTransaction({
        'from': account_obj.address,
        'nonce': w3.eth.getTransactionCount(account_obj.address),
        'gas': 1728712,
        'gasPrice': w3.toWei('21', 'gwei')}
)

signed = account_obj.signTransaction(txn)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

def wait_for_receipt(w3, tx_hash, poll_interval):
   while True:
       tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       if tx_receipt:
         return tx_receipt
       time.sleep(poll_interval)


wait_for_receipt(w3, tx_hash, 1)



print('Balance of "New" : {}'.format(
    MyC_contract.functions.balanceOf("0x0EFFab286B4F499D2F37a886B1EA4dFBCcfbC5de").call()
))

