from functions.payloads import criptoFacil_url, criptoFacil_payloads, copter_url,\
    copter_payloads, ripio_url, ripio_payloads
from functions.functions import get_crypto_currency_prices_from_payload, get_crypto_currency_prices
from model.cryptoCurrency_model import CryptoCurrency
from functions.payloads import CRYPTO_PAYLOAD_LIST
import unittest


class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.cryptoFacil = CryptoCurrency(criptoFacil_url, criptoFacil_payloads)
        self.copter = CryptoCurrency(copter_url, copter_payloads)
        self.ripio = CryptoCurrency(ripio_url, ripio_payloads)
        self.CRYPTO_LIST = CRYPTO_PAYLOAD_LIST
        self.crypto_list = []

    def tearDown(self):
        pass

    def testCryptoListIsEmpty(self):
        self.assertEqual(self.crypto_list, [])

    def testCryptoFacilValues(self):
        url = self.cryptoFacil.get_url()
        param = self.cryptoFacil.get_parameter()
        cryptoFacil = get_crypto_currency_prices(url, param)
        length_values = len(cryptoFacil.get_values())
        crypto_name = cryptoFacil.get_crypto_name()

        self.assertEqual(crypto_name, 'CRIPTOFACIL')
        self.assertEqual(length_values, 4)

    def testCopterValues(self):
        url = self.copter.get_url()
        param = self.copter.get_parameter()
        copter = get_crypto_currency_prices(url, param)
        length_values = len(copter.get_values())
        crypto_name = copter.get_crypto_name()

        self.assertEqual(crypto_name, 'COPTER')
        self.assertEqual(length_values, 1)

    def testRipioValues(self):
        url = self.ripio.get_url()
        param = self.ripio.get_parameter()
        ripio = get_crypto_currency_prices(url, param)
        length_values = len(ripio.get_values())
        crypto_name = ripio.get_crypto_name()

        self.assertEqual(crypto_name, 'RIPIO')
        self.assertEqual(length_values, 5)

    def testQuantityCryptoIsThree(self):
        self.crypto_list.append(self.cryptoFacil)
        self.crypto_list.append(self.copter)
        self.crypto_list.append(self.ripio)

        self.assertEqual(len(self.crypto_list), 3)

    def testQuantityCryptoPayloadIsEigth(self):
        crypto_value_list = get_crypto_currency_prices_from_payload(self.CRYPTO_LIST)
        crypto_prices_list = len(crypto_value_list)

        self.assertEqual(crypto_prices_list, 8)


if __name__ == '__main__':
    unittest.main()
