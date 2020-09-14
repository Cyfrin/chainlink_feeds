import os
from web3 import Web3
import configparser
import requests


class ChainlinkData(object):
    """ Base class where the decorators and base function for the other
    classes of this python wrapper will inherit from.
    """

    def __init__(self, rpc_url=None, output_format='json', proxy=None, rpc_env_var='RPC_URL'):
        """ Initialize the class
        Keyword Arguments:
            key:  rpc_url: The Ethereum Client node. This can be from node hosting services like infura, fiews, or quiknode.
            output_format:  Either 'json', 'pandas', or 'csv'
            proxy:  Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
        """
        if rpc_url is None:
            try:
                rpc_url = os.getenv(rpc_env_var)
            except:
                pass
        if not rpc_url or not isinstance(rpc_url, str):
            raise ValueError(
                'No value RPC_URL provided. Please set environment variable RPC_URL, provide an rpc_url as a keyword argument, or set your own environment variable name with rpc_env_var.')
        self.abi_config = configparser.ConfigParser().read('config/abis.config')
        self.addresses_config = configparser.ConfigParser().read('config/address.config')
        self.web3 = Web3(Web3.HTTPProvider(os.getenv(rpc_url)))
        self.proxy = proxy or {}
        self.output_format = output_format

    def get_latest_price(self, network='KOVAN', pair='ETH_USD'):
        address = self.addresses_config[network.upper()][pair.upper()]
        abi = self.abis_config['AGGREGATORV3INTERFACEABI']
        price_feed_contract = web3.eth.contract(address=address, abi=abi)
        return(latestData)

    def get_latest_round_data(self, network='KOVAN', pair='ETH_USD'):
        pass
