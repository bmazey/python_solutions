from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer


def main():
    BtcPricer.get_btc_usd_price_response()
    EthPricer.get_eth_usd_price_response()


if __name__ == '__main__':
    main()
