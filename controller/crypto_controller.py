from functions.functions import get_values_crypto_list, get_crypto_prices


class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_crypto_currency_prices(self):
        url = self.model.get_url()
        parameters = self.model.get_parameter()
        crypto = get_crypto_prices(url=url, payloads=parameters)

        self.view.show_crypto_currency(crypto.get_crypto_name(),
                                       crypto.get_time(),
                                       crypto.get_values())

    def show_crypto_currency_prices_list(self):
        crypto_list = self.model.get_crypto_currency_list()
        crypto_prices = get_values_crypto_list(crypto_list)

        crypto_names = [value.get_crypto_name() for value in crypto_prices]
        crypto_time = [value.get_time() for value in crypto_prices]
        crypto_values = [value.get_values() for value in crypto_prices]

        self.view.show_cryptos_currency_list(crypto_names,
                                             crypto_time,
                                             crypto_values)
