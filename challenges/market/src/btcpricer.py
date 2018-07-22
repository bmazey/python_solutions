import requests
import json


class BtcPricer:
    def __init__(self):
        # you will need to research the 'requests' module
        # you will need to read documentation: https://www.kraken.com/help/api
        # meet my friend json: json.org
        # do nothing in this constructor (normally security goes here ...)
        return

    @staticmethod
    def get_btc_usd_price_status():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return response

    @staticmethod
    def get_btc_usd_price_response():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return json.dumps(response.json())

    @staticmethod
    def get_btc_usd_price():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        price = response.json().get('result').get('XXBTZUSD').get('o')
        return price

    @staticmethod
    def get_btc_cad_price():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTCAD')
        price = response.json().get('result').get('XXBTZCAD').get('o')
        return price
