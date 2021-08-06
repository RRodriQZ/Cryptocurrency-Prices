class CryptoCurrency(object):
    def __init__(self, url: str, parameter: list) -> None:
        self._url = url
        self._parameter = parameter

    def get_url(self) -> str:
        return self._url

    def get_parameter(self) -> list:
        return self._parameter

    def __str__(self) -> str:
        return f"url: {self.get_url()}, parameters: {self.get_parameter()}"
