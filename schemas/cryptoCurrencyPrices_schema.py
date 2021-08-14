from model.cryptoCurrencyPrices_model import CryptoCurrencyPrices
from marshmallow import Schema, fields, post_load


class CurrencyValues(Schema):
    """CurrencyValues Schema"""

    parameters = fields.Dict(attribute="parameters")
    purchase_without_commissions = fields.Float(attribute="purchase_without_commissions")
    purchase_with_commissions = fields.Float(attribute="purchase_with_commissions")
    sale_without_commissions = fields.Float(attribute="sale_without_commissions")
    sale_with_commissions = fields.Float(attribute="sale_with_commissions")


class CryptoCurrencyPricesSchema(Schema):
    """CryptoCurrencyPrices Schema"""

    crypto_name = fields.String(attribute="crypto_name")
    time = fields.String(attribute="time")
    values = fields.List(fields.Nested(CurrencyValues))

    @post_load
    def create_crypto_currency_prices(self, data, **kwargs):
        return CryptoCurrencyPrices(**data)
