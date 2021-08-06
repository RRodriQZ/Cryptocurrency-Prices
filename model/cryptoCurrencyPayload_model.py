class CryptoCurrencyPayload(object):
    def __init__(self, cripto_prices_list: list) -> None:
        self._cripto_prices_list = cripto_prices_list

    def get_crypto_prices_payload_list(self) -> list:
        return self._cripto_prices_list

    def __str__(self) -> str:
        return f"[PAYLOAD]: {self.get_crypto_prices_payload_list()}"
