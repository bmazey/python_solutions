import requests


class EthPricer:
    def __init__(self):
        # do nothing (normally security here ... )
        return

    @staticmethod
    def get_eth_usd_price_response():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        print(response.json())