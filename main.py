from functions.functions import get_crypto_currency_prices_from_payload
from model.cryptoCurrencyPayload_model import CryptoCurrencyPayload
from crypto.cryptos import CryptoArgentBTC, CryptosB
from controller.crypto_controller import Controller
from functions.payloads import CRYPTO_PAYLOAD_LIST
from view.crypto_view import View


def main() -> None:
    # Example with "argenBTC", parameters extracted from Payload
    controller = Controller(CryptoArgentBTC(), View())
    controller.show_crypto_currency_prices()

    # Example with Cryptos with "B" in the initial of the exchange
    controller2 = Controller(CryptosB(), View())
    controller2.show_crypto_currency_prices_list()

    # Example with the list of cryptocurrencies
    crypto_payload_list = get_crypto_currency_prices_from_payload(crypto_payloads=CRYPTO_PAYLOAD_LIST)
    controller3 = Controller(CryptoCurrencyPayload(crypto_payload_list), View())
    controller3.show_crypto_currency_prices_payload()


if __name__ == "__main__":
    main()
