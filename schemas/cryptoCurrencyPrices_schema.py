from model.cryptoCurrencyPrices_model import CryptoCurrencyPrices
from marshmallow import Schema, fields, post_load


class CurrencyValues(Schema):
    """CurrencyValues Schema"""

    parametros = fields.Dict(attribute="parametros")
    compra_sin_comisiones = fields.Float(attribute="compra_sin_comisiones")
    compra_con_comisiones = fields.Float(attribute="compra_con_comisiones")
    venta_sin_comisiones = fields.Float(attribute="venta_sin_comisiones")
    venta_con_comisiones = fields.Float(attribute="venta_con_comisiones")


class CryptoCurrencyPricesSchema(Schema):
    """CryptoCurrencyPrices Schema"""

    crypto_name = fields.String(attribute="crypto_name")
    time = fields.String(attribute="time")
    values = fields.List(fields.Nested(CurrencyValues))

    @post_load
    def create_crypto_currency_prices(self, data, **kwargs):
        return CryptoCurrencyPrices(**data)
