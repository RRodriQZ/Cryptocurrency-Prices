from model.cryptoCurrency_model import CryptoCurrency
from functions.payloads import (
    bitex_payloads,
    bitex_url,
    bitso_payloads,
    bitso_url,
    buda_payloads,
    buda_url,
    buenbit_payloads,
    buenbit_url,
)


class CryptosB(object):
    def __init__(self):
        self.bitex = CryptoCurrency(bitex_url, bitex_payloads)
        self.bitso = CryptoCurrency(bitso_url, bitso_payloads)
        self.buda = CryptoCurrency(buda_url, buda_payloads)
        self.buenbit = CryptoCurrency(buenbit_url, buenbit_payloads)

    def get_crypto_currency_list(self):
        return [self.bitex, self.bitso, self.buda, self.buenbit]
