from dataclasses import dataclass


@dataclass
class CryptoCurrencyPayload(object):
    """Class represents CryptoCurrencyPayload model field: cripto_prices_list"""

    cripto_prices_list: list

    def get_crypto_prices_payload_list(self) -> list:
        return self.cripto_prices_list

    def __str__(self) -> str:
        return f"[PAYLOAD]: {self.get_crypto_prices_payload_list()}"
