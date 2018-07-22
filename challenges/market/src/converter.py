from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer


def main():
    # this is for experiments only! test does not look here ...
    print(BtcPricer.get_btc_usd_price_status())
    print(EthPricer.get_eth_usd_price_status())

    print(BtcPricer.get_btc_usd_price_response())
    print(EthPricer.get_eth_usd_price_response())

    print(BtcPricer.get_btc_usd_price())
    print(EthPricer.get_eth_usd_price())

    print(BtcPricer.get_btc_cad_price())
    print(EthPricer.get_eth_cad_price())


if __name__ == '__main__':
    main()
