import requests


class BtcPricer:
    def __init__(self):
        # do nothing (normally security goes here ...)
        return

    @staticmethod
    def get_btc_usd_price_response():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        print(response.json())
