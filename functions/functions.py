from schemas.validate_schema import validate_crypto_prices_for_schema
from model.cryptoCurrency_model import CryptoCurrency
from model.cryptoPrices_model import CryptoPrices
from datetime import datetime
from log.logger import Log
import requests

# GLOBAL VALUES #
logger = Log().getLogger(__name__)


def get_crypto_name_by_url(url: str) -> str:
    """ Retorno el nombre de exchange en mayuscula. """
    return url.split('/')[4].upper()


def get_str_time_now() -> str:
    """ Retorno la fecha actual en formato de String. """
    return datetime.now().strftime('%H:%M:%S %d-%m-%Y')


def get_str_payload(payload: dict) -> str:
    """ Retorno el payload de parametros en formato de string apendeado de: '/'.

    :param payload: dict
    :return: str
    """
    try:
        payload_str = ""
        for p in payload:
            payload_str = payload_str + '/' + str(payload[p])

        return payload_str
    except Exception as e:
        logger.error(f'Error en la transformacion del payload'
                     f' de los parametros, {e}')


def get_url_complete_with_payload(url: str, payload: dict) -> str:
    """ Retorno la URL completa junto con su payload para llamar a la API. """
    payload = get_str_payload(payload)
    url_complete = url + payload

    return url_complete


def get_response_by_url(url: str) -> dict:
    """ Retorno el response json del llamado a la API.

    :param url: str
    :return: dict
    """
    try:
        response = requests.get(url=url, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f'Error en el retorno del response de '
                     f'url: "{url}", error: "{e}"')


def get_values_from_crypto_result(url: str, payloads: list[dict]) -> list[dict]:
    """ Retorna el crypto_json con sus llamados por paramentos de
    cambio de la moneda.

    :param url: str
    :param payloads: list[dict]
    :return: list[dict]
    """
    try:
        result_list = []

        for payload in payloads:
            crypto_result = dict()
            URL = get_url_complete_with_payload(url, payload)

            results = get_response_by_url(URL)

            crypto_result['Parametros'] = payload
            crypto_result['Compra_sin_comisiones'] = results['ask']
            crypto_result['Compra_con_comisiones'] = results['totalAsk']
            crypto_result['Venta_sin_comisiones'] = results['bid']
            crypto_result['Venta_con_comisiones'] = results['totalBid']

            result_list.append(crypto_result)

        return result_list

    except Exception as e:
        logger.error(f'Error al llamar a la API, error: "{e}"')


def get_crypto_prices(url: str, payloads: list[dict]) -> CryptoPrices:
    """ Retorno el nuevo CryptoPrices armado con todos sus valores
    llamados de su parameters.

    :param url: str
    :param payloads: list[dict]
    :return: CryptoPrices
    """
    try:
        crypto_name = get_crypto_name_by_url(url)
        time_now = get_str_time_now()
        result_json_list = get_values_from_crypto_result(url, payloads)

        evaluate_crypto = {"crypto_name": crypto_name,
                           "time": time_now,
                           "values": result_json_list}

        validate_crypto_prices_for_schema(evaluate_crypto)

        new_crypto = CryptoPrices(crypto_name, time_now, result_json_list)
        logger.info(f'Obtenido correctamente: {new_crypto.__str__()}')

        return new_crypto

    except Exception as e:
        logger.error(f'Error en la obtencion de valores, error: "{e}"')


def get_values_crypto_list(crypto_list: list[CryptoCurrency]) -> list[CryptoPrices]:
    """ Retorno una la lista de Cryptos que llamaron a la API.

    :param crypto_list: list[CryptoCurrency]
    :return: list[CryptoPrices]
    """
    try:
        logger.info(f'===========[ INICIANDO LA LISTA LLAMADOS A '
                    f'LA API DE CRYPTOYA ]===========')

        crypto_prices_list = []

        for crypto in crypto_list:
            url = crypto.get_url()
            param = crypto.get_parameter()
            crypto_prices = get_crypto_prices(url, param)

            crypto_prices_list.append(crypto_prices)

        return crypto_prices_list

    except Exception as e:
        logger.error(f'Error en la obtencion de currency prices, error: "{e}"')


def get_all_values_from_payload(payload_cryptos: list) -> list[CryptoPrices]:
    """ Retorno una la lista de Cryptos que llamaron a la API desde el PAYLOAD.

    :param payload_cryptos: list
    :return: list[CryptoPrices]
    """
    try:
        logger.info(f'=========[ LLAMANDO CON EL PAYLOAD A '
                    f'LA API DE CRYPTOYA ]=========')

        crypto_list = []

        for crypto in payload_cryptos:
            crypto_currency = get_crypto_prices(crypto[0], crypto[1])
            crypto_list.append(crypto_currency)

        return crypto_list

    except Exception as e:
        logger.error(f'Error en la obtencion de currency prices del PAYLOAD,'
                     f' error: "{e}"')
