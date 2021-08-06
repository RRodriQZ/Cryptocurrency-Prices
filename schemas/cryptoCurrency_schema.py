from model.cryptoCurrency_model import CryptoCurrency
from marshmallow import Schema, fields, post_load


class CryptoCurrencySchema(Schema):
    """CryptoCurrency Schema"""

    url = fields.String(attribute="url")
    parameter = fields.List(fields.Dict(attribute="parameter"))

    @post_load
    def create_crypto_currency(self, data, **kwargs):
        return CryptoCurrency(**data)
