from dataclasses import dataclass


@dataclass
class CryptoCurrency(object):
    """Class represents CryptoCurrency model fields: url & parameter"""

    url: str
    parameter: list[dict]

    def get_url(self) -> str:
        return self.url

    def get_parameter(self) -> list:
        return self.parameter

    def __str__(self) -> str:
        return f"url: {self.get_url()}, parameters: {self.get_parameter()}"
