import time
from eth_account import Account


class conf:
    import json
    import time
    import os
    from eth_account import Account
    from web3 import Web3
    w3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/032b2cbaaefc4ad5b7fc1a875fbed094", websocket_kwargs={'timeout': 60}))
    acc = "0x841B02Fe7951B0F14EAa8329f0F62a32EEEc6283"
    user_account = "aa"
    w3.eth.defaultAccount = acc
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(PROJECT_ROOT, "abi.py")) as f:
        info_json = json.load(f)
    abi = info_json
    contract_address = "0xea409026765aff2ecfa5a1c88436dd8d137f00c1"
    contract_address = "0x2083eeca384d40968549ad9d06e24b09edb951d0"
    MyC_contract = w3.eth.contract(address=w3.toChecksumAddress(contract_address), abi=abi)
    account_obj = Account.privateKeyToAccount(b"c\x15\x19\xc8\xc1\xf3GV\x07[65\xf8\x89Ul\xa8\x9e$\xff\xf6;\xdeK\x14'\x81;g\xc6\xa2\xcd")

    def wait_for_receipt(w3, tx_hash, poll_interval):
        while True:
            tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
            if tx_receipt:
                return tx_receipt
            time.sleep(poll_interval)


    def set_userAccount(user_account):
        conf.user_account = user_account

    def get_userAccount(self):
        return conf.user_account

    def getAccountFromPrivateKey(key):
        account_obj = Account.privateKeyToAccount(key)
        return account_obj

###
    #0x5E57AfDCa6a3Da629C5efecdaA1e06C1d80715d2
###



# app{
# 0x5E57AfDCa6a3Da629C5efecdaA1e06C1d80715d2
# b"c\x15\x19\xc8\xc1\xf3GV\x07[65\xf8\x89Ul\xa8\x9e$\xff\xf6;\xdeK\x14'\x81;g\xc6\xa2\xcd"
# 0x631519c8c1f34756075b3635f889556ca89e24fff63bde4b1427813b67c6a2cd
# }


#
# wwwadspihfgrorft
# account Created
# 0x186DEB1c2E9a62ACac21B0FdD4e9105E4f65B0A6
# 0xaf3cd5e1792ce8039f20afb496106cfb4f906fafb85cf07b9dab286c50fa3c59