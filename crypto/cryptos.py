from schemas.cryptoCurrency_schema import CryptoCurrencySchema
from functions.payloads import CRYPTO_PAYLOAD_LIST
from functions.payloads import (
    argenBTC_url,
    argenBTC_payloads,
    bitex_payloads,
    bitex_url,
    bitso_payloads,
    bitso_url,
    buda_payloads,
    buda_url,
    buenbit_payloads,
    buenbit_url,
)


class CryptoArgentBTC(object):
    def __init__(self):
        self.ArgentBTC = CryptoCurrencySchema().load(
            {"url": argenBTC_url, "parameter": argenBTC_payloads}
        )

    def get_ArgentBTC_currency(self):
        return self.ArgentBTC


class CryptosB(object):
    def __init__(self):
        self.bitex = CryptoCurrencySchema().load(
            {"url": bitex_url, "parameter": bitex_payloads}
        )
        self.bitso = CryptoCurrencySchema().load(
            {"url": bitso_url, "parameter": bitso_payloads}
        )
        self.buda = CryptoCurrencySchema().load(
            {"url": buda_url, "parameter": buda_payloads}
        )
        self.buenbit = CryptoCurrencySchema().load(
            {"url": buenbit_url, "parameter": buenbit_payloads}
        )

    def get_crypto_currency_list(self):
        return [self.bitex, self.bitso, self.buda, self.buenbit]
