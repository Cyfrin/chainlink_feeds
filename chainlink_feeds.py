import os
from web3 import Web3
import configparser
import logging as log
from functools import wraps
from datetime import datetime
import json
log.basicConfig(level=log.INFO)


def _output_formatter(func):
    @wraps(func)
    def _conversion_formating(self, *args, **kwargs):
        result_dict = func(self, *args, **kwargs)
        result_dict['price'] = float(self.web3.fromWei(
            result_dict['price'], self.conversion))
        if self.time is not None:
            result_dict['time_stamp'] = datetime.fromtimestamp(
                result_dict['time_stamp']).strftime(self.time)
            result_dict['started_at'] = datetime.fromtimestamp(
                result_dict['started_at']).strftime(self.time)
        return result_dict
    return _conversion_formating


class ChainlinkFeeds(object):
    """ Base class where the decorators and base function for the other
    classes of this python wrapper will inherit from.

    TODO: Add The Graph for historical
    """

    def __init__(self, rpc_url=None, output_format='json', proxy=None, rpc_env_var='RPC_URL', conversion='ether', time='%Y-%m-%d %H:%M:%S'):
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
        self.abis_config = configparser.ConfigParser()
        self.addresses_config = configparser.ConfigParser()
        self.load_config(os.path.join(os.path.dirname(
            __file__), 'config', 'addresses.cfg'), abi_or_address='address')
        self.load_config(os.path.join(os.path.dirname(
            __file__), 'config', 'abis.cfg'), abi_or_address='abi')
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.proxy = proxy or {}
        self.output_format = output_format
        self.conversion = conversion
        self.time = time

    @_output_formatter
    def get_latest_round_data(self, network='kovan', pair='eth_usd', address=None, abi=None):
        """Pairs that end with ETH have 18 0s. All other pairs only have 10.
        We multiply them by 'bump' so they are all in wei before conversion.
        """
        bump = 1
        if not pair.endswith('ETH'):
            bump = 10000000000
        if address is None:
            address = self.addresses_config[network.lower()][pair]
        if abi is None:
            abi = self.abis_config['default']['aggregatorv3interfaceabi']
        price_feed_contract = self.web3.eth.contract(address=address, abi=abi)
        latest_data = price_feed_contract.functions.latestRoundData().call()
        result_dict = {'round_id': latest_data[0], 'price': latest_data[1] * bump,
                       'started_at': latest_data[2], 'time_stamp': latest_data[3], 'answered_in_round': latest_data[4]}
        return result_dict

    @_output_formatter
    def get_historical_price(self, round_id, network='kovan', pair='eth_usd', address=None, abi=None):
        """Pairs that end with ETH have 18 0s. All other pairs only have 10.
        We multiply them by 'bump' so they are all in wei before conversion.
        """
        bump = 1
        if not pair.endswith('eth'):
            bump = 10000000000
        if address is None:
            address = self.addresses_config[network.lower()][pair]
        if abi is None:
            abi = self.abis_config['default']['aggregatorv3interfaceabi']
        price_feed_contract = self.web3.eth.contract(address=address, abi=abi)
        latest_data = price_feed_contract.functions.getRoundData(
            round_id).call()
        result_dict = {'round_id': latest_data[0], 'price': latest_data[1] * bump,
                       'started_at': latest_data[2], 'time_stamp': latest_data[3], 'answered_in_round': latest_data[4]}
        return result_dict

    def load_config(self, config_path, abi_or_address='abi'):
        if abi_or_address.lower() == 'abi':
            self.abis_config.read(config_path)
        else:
            self.addresses_config.read(config_path)

    def get_addresses(self):
        return json.loads(json.dumps(self.addresses_config._sections))

    def get_abis(self):
        return json.loads(json.dumps(self.abis_config._sections))

    def get_historical_prices():
        pass
