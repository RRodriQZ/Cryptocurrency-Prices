from schemas.cryptoCurrencyPrices_schema import CryptoCurrencyPricesSchema
from model.cryptoCurrencyPrices_model import CryptoCurrencyPrices
from model.cryptoCurrency_model import CryptoCurrency
from datetime import datetime
from log.logger import Log
import requests


# GLOBAL VALUES #
logger = Log().getLogger(__name__)
time_out = 20


def get_crypto_name_by_url(url: str) -> str:
    """Retorno el nombre de exchange en mayuscula"""
    return url.split("/")[4].upper()


def get_str_time_now() -> str:
    """Retorno la fecha actual en formato de String"""
    return datetime.now().strftime("%H:%M:%S %d-%m-%Y")


def get_str_payload(payload: dict) -> str:
    """Retorno el payload de parametros en formato de string apendeado de: '/'

    :param payload: dict
    :return: str
    """
    try:
        payload_str = ""
        for p in payload:
            payload_str = payload_str + "/" + str(payload[p])
        return payload_str

    except Exception as e:
        logger.error(f'Error en la transformacion del payload de los parametros, "{e}"')


def get_url_complete(url: str, payload: dict) -> str:
    """Retorno la URL completa junto con su payload para llamar a la API

    :param url: str
    :param payload: dict
    :return: str
    """
    try:
        payload = get_str_payload(payload=payload)
        url_complete = url + payload
        return url_complete

    except Exception as e:
        logger.error(f'Error en el retorno de la URL completa, error: "{e}"')


def get_response_by_url(url: str) -> dict:
    """Retorno el response json del llamado a la API

    :param url: str
    :return: dict
    """
    try:
        response = requests.get(url=url, timeout=time_out)
        return response.json()

    except Exception as e:
        logger.error(f'Error en el retorno del response de url: "{url}", error: "{e}"')


def get_crypto_currency_values_json(url: str, payloads: list[dict]) -> list[dict]:
    """Retorna el crypto_json con sus llamados por paramentos de cambio de la moneda

    :param url: str
    :param payloads: list[dict]
    :return: list[dict]
    """
    try:
        result_list = []

        for payload in payloads:
            crypto_result = dict()
            URL = get_url_complete(url=url, payload=payload)

            results = get_response_by_url(url=URL)

            crypto_result["parametros"] = payload
            crypto_result["compra_sin_comisiones"] = results["ask"]
            crypto_result["compra_con_comisiones"] = results["totalAsk"]
            crypto_result["venta_sin_comisiones"] = results["bid"]
            crypto_result["venta_con_comisiones"] = results["totalBid"]

            result_list.append(crypto_result)

        return result_list

    except Exception as e:
        logger.error(f'Error al llamar a la API, error: "{e}"')


def get_crypto_currency_prices(url: str, payloads: list[dict]) -> CryptoCurrencyPrices:
    """Retorno el nuevo CryptoPrices armado con todos sus valores llamados de su parameters

    :param url: str
    :param payloads: list[dict]
    :return: CryptoCurrencyPrices
    """
    try:
        crypto_name = get_crypto_name_by_url(url)
        time = get_str_time_now()
        values = get_crypto_currency_values_json(url, payloads)

        new_crypto = CryptoCurrencyPricesSchema().load(
            {"crypto_name": crypto_name, "time": time, "values": values}
        )

        logger.info(f"* Obtenido correctamente: {new_crypto.__str__()}")

        return new_crypto

    except Exception as e:
        logger.error(f'Error en la obtencion de valores, error: "{e}"')


def get_crypto_prices(crypto: CryptoCurrency) -> CryptoCurrencyPrices:
    url = crypto.get_url()
    parameters = crypto.get_parameter()
    crypto_prices = get_crypto_currency_prices(url=url, payloads=parameters)

    return crypto_prices


def get_crypto_currency_prices_from_list(crypto_list: list[CryptoCurrency]) -> list[CryptoCurrencyPrices]:
    """Retorno una la lista de Cryptos que llamaron a la API

    :param crypto_list: list[CryptoCurrency]
    :return: list[CryptoCurrencyPrices]
    """
    try:
        logger.info(
            f"***********[ INICIANDO LA LISTA LLAMADOS A LA API DE CRYPTOYA ]***********"
        )

        crypto_prices_list = []

        for crypto in crypto_list:

            crypto_prices = get_crypto_prices(crypto=crypto)

            crypto_prices_list.append(crypto_prices)

        return crypto_prices_list

    except Exception as e:
        logger.error(f'Error en la obtencion de currency prices, error: "{e}"')


def get_crypto_currency_prices_from_payload(crypto_payloads: list) -> list[CryptoCurrencyPrices]:
    """Retorno una la lista de Cryptos que llamaron a la API desde el PAYLOAD

    :param crypto_payloads: list
    :return: list[CryptoCurrencyPrices]
    """
    try:
        logger.info(
            f"=========[ LLAMANDO CON EL PAYLOAD A LA API DE CRYPTOYA ]========="
        )

        crypto_list = []

        for crypto in crypto_payloads:
            url = crypto[0]
            payload = crypto[1]
            crypto_currency = get_crypto_currency_prices(url=url, payloads=payload)
            crypto_list.append(crypto_currency)

        return crypto_list

    except Exception as e:
        logger.error(
            f'Error en la obtencion de currency prices del PAYLOAD, error: "{e}"'
        )
