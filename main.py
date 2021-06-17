from functions.payloads import argenBTC_url, argenBTC_payloads
from model.cryptoCurrency_model import CryptoCurrency
from controller.crypto_controller import Controller
from crypto.cryptos_B import CryptosB
from view.crypto_view import View


if __name__ == '__main__':
    # Ejemplo con "argenBTC", parametros extraidos del Payload
    argenBTC = CryptoCurrency(argenBTC_url, argenBTC_payloads)
    controller = Controller(argenBTC, View())
    controller.show_crypto_currency_prices()

    # Ejemplo con Cryptos con "B" en la inicial del exchange
    controller2 = Controller(CryptosB(), View())
    controller2.show_crypto_currency_prices_list()
