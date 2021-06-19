from functions.payloads import argenBTC_url, argenBTC_payloads, CRYPTO_PAYLOAD_LIST
from functions.functions import get_crypto_currency_prices_from_payload
from model.cryptoCurrencyPayload_model import CryptoCurrencyPayload
from model.cryptoCurrency_model import CryptoCurrency
from controller.crypto_controller import Controller
from crypto.cryptos_B import CryptosB
from view.crypto_view import View


if __name__ == '__main__':
    # Ejemplo con "argenBTC", parametros extraidos del Payload
    controller = Controller(CryptoCurrency(argenBTC_url, argenBTC_payloads), View())
    controller.show_crypto_currency_prices()

    # Ejemplo con Cryptos con "B" en la inicial del exchange
    controller2 = Controller(CryptosB(), View())
    controller2.show_crypto_currency_prices_list()

    # Ejemplo con el Payload Completo
    crypto_payload_list = get_crypto_currency_prices_from_payload(CRYPTO_PAYLOAD_LIST)
    controller3 = Controller(CryptoCurrencyPayload(crypto_payload_list), View())
    controller3.show_crypto_currency_prices_payload()
