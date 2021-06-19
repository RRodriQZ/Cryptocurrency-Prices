# CRYPTO VALUES #
argenBTC_url = 'https://criptoya.com/api/argenbtc'
bitex_url = 'https://criptoya.com/api/bitex/btc'
bitso_url = 'https://criptoya.com/api/bitso'
buda_url = 'https://criptoya.com/api/buda'
buenbit_url = 'https://criptoya.com/api/buenbit'
copter_url = 'https://criptoya.com/api/copter'
criptoFacil_url = 'https://criptoya.com/api/criptofacil'
ripio_url = 'https://criptoya.com/api/ripio'

argenBTC_payloads = [{}]

bitex_payloads = [{'fiat': 'ARS', 'vol': 0.5},
                  {'fiat': 'USD', 'vol': 0.5},
                  {'fiat': 'ARS', 'vol': 1},
                  {'fiat': 'USD', 'vol': 1}
                  ]

bitso_payloads = [{"coin": "BTC", "fiat": "ARS", "vol": 500},
                  {"coin": "BTC", "fiat": "USD", "vol": 1},
                  {"coin": "DAI", "fiat": "ARS", "vol": 1}
                  ]

buda_payloads = [{'coin': 'BTC', "fiat": "ARS", 'vol': 0.5},
                 {'coin': 'ETH', "fiat": "ARS", 'vol': 0.5},
                 {'coin': 'BCH', "fiat": "ARS", 'vol': 0.5},
                 {'coin': 'LTC', "fiat": "ARS", 'vol': 0.5}
                 ]

buenbit_payloads = [{'coin': 'BTC', 'fiat': 'ARS'},
                    {'coin': 'DAI', 'fiat': 'ARS'},
                    {'coin': 'DAI', 'fiat': 'USD'},
                    ]

copter_payloads = [{'coin': 'BTC', 'fiat': 'ARS', 'vol': 1}
                   ]

criptoFacil_payloads = [{'coin': 'BTC'},
                        {'coin': 'ETH'},
                        {'coin': 'USDT'},
                        {'coin': 'ADA'}
                        ]

ripio_payloads = [{'coin': 'BTC'},
                  {'coin': 'ETH'},
                  {'coin': 'DAI'},
                  {'coin': 'USDC'},
                  {'coin': 'LTC'}
                  ]

CRYPTO_PAYLOAD_LIST = [
    [argenBTC_url,     argenBTC_payloads],
    [bitex_url,        bitex_payloads],
    [bitso_url,        bitso_payloads],
    [buda_url,         buda_payloads],
    [buenbit_url,      buenbit_payloads],
    [copter_url,       copter_payloads],
    [criptoFacil_url,  criptoFacil_payloads],
    [ripio_url,        ripio_payloads]
]
