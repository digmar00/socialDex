from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/'
                            '0105fce4a7c848c18d3bf9b2110d7f21'))

account = w3.eth.account.create()
private_key = account.privateKey.hex()
address = account.address

print("Your address is:{}\nYour private key is:{}".format(address, private_key))

