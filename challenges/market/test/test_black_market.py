import json
import krakenex
from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer


'''
Welcome to the Black Market Challenge! 

You must have an Internet connection at all times when working on or testing this challenge.
Your goal is simple: get the price of Bitcoin and Ethereum in two different fiat currencies.

Do your research and use Postman. If your connection is slow, you may get test failures even with correct solutions.

Note: You are prohibited from using the krakenx module in your solution!
'''


def test_price_response_status():
    # get the response status code
    assert str(BtcPricer.get_btc_usd_price_status()) == '<Response [200]>'
    assert str(EthPricer.get_eth_usd_price_status()) == '<Response [200]>'


def test_price_response_format():
    # make sure response is valid json
    assert json.loads((BtcPricer.get_btc_usd_price_response()))
    assert json.loads((EthPricer.get_eth_usd_price_response()))


def test_usd_price():
    # get the usd price
    # you are not allowed to use krakenex in your solution
    kraken = krakenex.API()
    bpair = {'pair': 'XBTUSD'}
    epair = {'pair': 'ETHUSD'}

    # offering leeway: the price can actually change during the test!
    assert abs(float(BtcPricer.get_btc_usd_price()) - float(kraken.query_public('Ticker', bpair)['result']['XXBTZUSD']['o'])) <= 1
    assert abs(float(EthPricer.get_eth_usd_price()) - float(kraken.query_public('Ticker', epair)['result']['XETHZUSD']['o'])) <= 1


def test_cad_price():
    # get the cad price
    # you are not allowed to use krakenex in your solution
    kraken = krakenex.API()
    bpair = {'pair': 'XBTCAD'}
    epair = {'pair': 'ETHCAD'}

    # offering leeway: the price can actually change during the test!
    assert abs(float(BtcPricer.get_btc_cad_price()) - float(kraken.query_public('Ticker', bpair)['result']['XXBTZCAD']['o'])) <= 2
    assert abs(float(EthPricer.get_eth_cad_price()) - float(kraken.query_public('Ticker', epair)['result']['XETHZCAD']['o'])) <= 2
