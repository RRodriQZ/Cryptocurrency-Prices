from functions.functions import get_crypto_currency_prices_from_list, get_crypto_prices


class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_crypto_currency_prices(self):
        crypto = get_crypto_prices(crypto=self.model.get_ArgentBTC_currency())

        self.view.show_crypto_currency(
            crypto_name=crypto.get_crypto_name(),
            crypto_time=crypto.get_time(),
            crypto_values=crypto.get_values(),
        )

    def show_crypto_currency_prices_list(self):
        crypto_list = self.model.get_crypto_currency_list()
        crypto_prices = get_crypto_currency_prices_from_list(crypto_list=crypto_list)

        crypto_names = [value.get_crypto_name() for value in crypto_prices]
        crypto_times = [value.get_time() for value in crypto_prices]
        crypto_values = [value.get_values() for value in crypto_prices]

        self.view.show_crypto_currency_list(
            crypto_name=crypto_names,
            crypto_time=crypto_times,
            crypto_values=crypto_values,
        )

    def show_crypto_currency_prices_payload(self):
        crypto_prices_payload = self.model.get_crypto_prices_payload_list()

        crypto_names = [value.get_crypto_name() for value in crypto_prices_payload]
        crypto_times = [value.get_time() for value in crypto_prices_payload]
        crypto_values = [value.get_values() for value in crypto_prices_payload]

        self.view.show_crypto_currency_list(crypto_names, crypto_times, crypto_values)
