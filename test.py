from schemas.cryptoCurrency_schema import CryptoCurrencySchema
from functions.payloads import CRYPTO_PAYLOAD_LIST
from functions.functions import (
    get_crypto_currency_prices_from_payload,
    get_crypto_currency_prices,
)
from functions.payloads import (
    criptoFacil_payloads,
    criptoFacil_url,
    copter_payloads,
    ripio_payloads,
    copter_url,
    ripio_url,
)
import unittest


class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.cryptoFacil = CryptoCurrencySchema().load({"url": criptoFacil_url, "parameter": criptoFacil_payloads})
        self.copter = CryptoCurrencySchema().load({"url": copter_url, "parameter": copter_payloads})
        self.ripio = CryptoCurrencySchema().load({"url": ripio_url, "parameter": ripio_payloads})
        self.CRYPTO_LIST = CRYPTO_PAYLOAD_LIST
        self.crypto_list = []

    def tearDown(self):
        pass

    def test_crypto_list_is_empty(self):
        self.assertEqual(self.crypto_list, [])

    def test_crypto_facil_values(self):
        url = self.cryptoFacil.get_url()
        parameter = self.cryptoFacil.get_parameter()
        cryptoFacil = get_crypto_currency_prices(url=url, payloads=parameter)
        length_values = len(cryptoFacil.get_values())
        crypto_name = cryptoFacil.get_crypto_name()

        self.assertEqual(crypto_name, "CRIPTOFACIL")
        self.assertEqual(length_values, 4)

    def test_copter_values(self):
        url = self.copter.get_url()
        param = self.copter.get_parameter()
        copter = get_crypto_currency_prices(url, param)
        length_values = len(copter.get_values())
        crypto_name = copter.get_crypto_name()

        self.assertEqual(crypto_name, "COPTER")
        self.assertEqual(length_values, 1)

    def test_ripio_values(self):
        url = self.ripio.get_url()
        parameter = self.ripio.get_parameter()
        ripio = get_crypto_currency_prices(url=url, payloads=parameter)
        length_values = len(ripio.get_values())
        crypto_name = ripio.get_crypto_name()

        self.assertEqual(crypto_name, "RIPIO")
        self.assertEqual(length_values, 5)

    def test_quantity_crypto_is_three(self):
        self.crypto_list.append(self.cryptoFacil)
        self.crypto_list.append(self.copter)
        self.crypto_list.append(self.ripio)

        self.assertEqual(len(self.crypto_list), 3)

    def test_quantity_crypto_payload_is_eigth(self):
        crypto_value_list = get_crypto_currency_prices_from_payload(crypto_payloads=self.CRYPTO_LIST)
        crypto_prices_list = len(crypto_value_list)

        self.assertEqual(crypto_prices_list, 8)


if __name__ == "__main__":
    unittest.main()
