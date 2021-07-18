class CryptoCurrencyPrices(object):
    def __init__(self, crypto_name: str, time: str, values: list[dict]) -> None:
        self._crypto_name = crypto_name
        self._time = time
        self._values = values

    def get_crypto_name(self) -> str:
        return self._crypto_name

    def get_time(self) -> str:
        return self._time

    def get_values(self) -> list[dict]:
        return self._values

    def __str__(self) -> str:
        return f'[Crypto]: "{self.get_crypto_name()}" [Time]: "{self.get_time()}" [Values]: {self.get_values()}'
