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
    """Returns the name of the exchange in uppercase"""
    return url.split("/")[4].upper()


def get_str_time_now() -> str:
    """Return the current date in String format"""
    return datetime.now().strftime("%H:%M:%S %d-%m-%Y")


def get_str_payload(payload: dict) -> str:
    """Return the parameter payload in string format depending on: '/'

    :param payload: dict
    :return: str
    """
    try:
        payload_str = ""
        for p in payload:
            payload_str = payload_str + "/" + str(payload[p])
        return payload_str

    except Exception as e:
        logger.error(f'Error in the transformation of the payload of the parameters, error: "{e}"')


def get_url_complete(url: str, payload: dict) -> str:
    """Return the full URL along with its payload to call the API

    :param url: str
    :param payload: dict
    :return: str
    """
    try:
        payload = get_str_payload(payload=payload)
        url_complete = url + payload
        return url_complete

    except Exception as e:
        logger.error(f'Full URL return failed, error: "{e}"')


def get_response_by_url(url: str) -> dict:
    """Return the json response of the API call

    :param url: str
    :return: dict
    """
    try:
        response = requests.get(url=url, timeout=time_out)
        return response.json()

    except Exception as e:
        logger.error(f'Error in the return of the url response: "{url}", error: "{e}"')


def get_crypto_currency_values_json(url: str, payloads: list) -> list:
    """Returns the crypto_json with its calls for currency exchange parameters

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

            crypto_result["parameters"] = payload
            crypto_result["purchase_without_commissions"] = results["ask"]
            crypto_result["purchase_with_commissions"] = results["totalAsk"]
            crypto_result["sale_without_commissions"] = results["bid"]
            crypto_result["sale_with_commissions"] = results["totalBid"]

            result_list.append(crypto_result)

        return result_list

    except Exception as e:
        logger.error(f'API call failed, error: "{e}"')


def get_crypto_currency_prices(url: str, payloads: list) -> CryptoCurrencyPrices:
    """Return the new CryptoPrices armed with all its values called from its parameters

    :param url: str
    :param payloads: list[dict]
    :return: CryptoCurrencyPrices
    """
    try:
        crypto_name = get_crypto_name_by_url(url=url)
        time = get_str_time_now()
        values = get_crypto_currency_values_json(url=url, payloads=payloads)

        new_crypto = CryptoCurrencyPricesSchema().load(
            {"crypto_name": crypto_name, "time": time, "values": values}
        )

        logger.info(f"* Successfully obtained: {new_crypto.__str__()}")

        return new_crypto

    except Exception as e:
        logger.error(f'Error in obtaining values, error: "{e}"')


def get_crypto_prices(crypto: CryptoCurrency) -> CryptoCurrencyPrices:
    """Return the price of crypto

    :param crypto: CryptoCurrency
    :return: CryptoCurrencyPrices
    """
    url = crypto.get_url()
    parameters = crypto.get_parameter()
    crypto_prices = get_crypto_currency_prices(url=url, payloads=parameters)

    return crypto_prices


def get_crypto_currency_prices_from_list(crypto_list: list) -> list:
    """Return a the list of Cryptos that called the API

    :param crypto_list: list[CryptoCurrency]
    :return: list[CryptoCurrencyPrices]
    """
    try:
        logger.info(
            f"***********[ STARTING THE LIST CALLED TO THE CRYPTOYA API ]***********"
        )

        crypto_prices_list = []

        for crypto in crypto_list:

            crypto_prices = get_crypto_prices(crypto=crypto)

            crypto_prices_list.append(crypto_prices)

        return crypto_prices_list

    except Exception as e:
        logger.error(f'Error in obtaining currency prices, error: "{e}"')


def get_crypto_currency_prices_from_payload(crypto_payloads: list) -> list:
    """Returns the list of Cryptos that called the API from PAYLOAD

    :param crypto_payloads: list
    :return: list[CryptoCurrencyPrices]
    """
    try:
        logger.info(
            f"=========[ CALLING THE CRYPTOYA API WITH PAYLOAD ]========="
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
            f'Error in obtaining currency prices from PAYLOAD, error: "{e}"'
        )
