from dataclasses import dataclass


@dataclass
class CryptoCurrencyPrices(object):
    """Class represents CryptoCurrencyPrices model fields: crypto_name, time & values"""

    crypto_name: str
    time: str
    values: list

    def get_crypto_name(self) -> str:
        return self.crypto_name

    def get_time(self) -> str:
        return self.time

    def get_values(self) -> list:
        return self.values

    def __str__(self) -> str:
        return f'[Crypto]: "{self.get_crypto_name()}" [Time]: "{self.get_time()}" [Values]: {self.get_values()}'
