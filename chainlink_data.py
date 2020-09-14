import os
from web3 import Web3
import configparser


class ChainlinkData(object):
    """ Base class where the decorators and base function for the other
    classes of this python wrapper will inherit from.
    """
    config = configparser.ConfigParser()
    config.read('config/abis.config')
    web3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

    def __init__(self, rpc_url=None, output_format='json', proxy=None, rpc_env_var='RPC_URL'):
        """ Initialize the class
        Keyword Arguments:
            key:  rpc_url: The Ethereum Client node. This can be from node hosting services like infura, fiews, or quiknode.
            output_format:  Either 'json', 'pandas', or 'csv'
            proxy:  Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
        """
        if rpc_url is None:
            rpc_url = os.getenv(rpc_env_var)
        if not rpc_url or not isinstance(rpc_url, str):
            raise ValueError(
                'No value RPC_URL provided. Please set environment variable RPC_URL, provide an rpc_url as a keyword argument, or set your own environment variable name with rpc_env_var.')
