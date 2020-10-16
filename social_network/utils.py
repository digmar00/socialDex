from web3 import Web3


def send_transaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/'
                                '0105fce4a7c848c18d3bf9b2110d7f21'))

    address = '0x97a384b952934465CCc84c5e86826cB7789d2403'
    private_key = '0x117e1579d71cec2577073de65ea8805397d40255ec05364bff46c31cd416f912'
    nonce = w3.eth.getTransactionCount(address)
    gas_price = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')

    signed_tx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gas_price,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), private_key)

    tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_id = w3.toHex(tx)

    return tx_id
