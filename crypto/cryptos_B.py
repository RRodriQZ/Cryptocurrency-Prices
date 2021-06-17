from functions.payloads import bitex_url, bitex_payloads, bitso_url,\
    bitso_payloads, buda_url, buda_payloads, buenbit_url, buenbit_payloads
from model.cryptoCurrency_model import CryptoCurrency


class CryptosB(object):
    def __init__(self):
        self.bitex = CryptoCurrency(bitex_url, bitex_payloads)
        self.bitso = CryptoCurrency(bitso_url, bitso_payloads)
        self.buda = CryptoCurrency(buda_url, buda_payloads)
        self.buenbit = CryptoCurrency(buenbit_url, buenbit_payloads)

    def get_crypto_currency_list(self):
        return [self.bitex, self.bitso, self.buda, self.buenbit]
