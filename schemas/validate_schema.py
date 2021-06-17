from jsonschema import validate
import json
import os


def validate_crypto_prices_for_schema(json_crypto: dict) -> None:
    file_path = os.path.join(os.path.dirname(__file__), 'crypto_schema.json')
    with open(file_path, 'r') as values:
        SCHEMA_CRYPTO = json.load(values)

    validate(instance=json_crypto, schema=SCHEMA_CRYPTO)
