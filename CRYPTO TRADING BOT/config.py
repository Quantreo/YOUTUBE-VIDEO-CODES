import ccxt
api = ccxt.bitget({
    'apiKey':"YOUR API KEY",
    'secret':"YOUR SECRET KEY",
    "password": "YOUT PASSWORD",
    'enableRateLimit': True,
    'timeout': 60000,
    'options': {
        'defaultType': 'spot',
    }
})

api.options['createMarketBuyOrderRequiresPrice'] = False