# content of conftest.py
import pytest
import logging as log

from ..chainlink_feeds import ChainlinkFeeds
log.basicConfig(level=log.INFO)


@pytest.fixture
def get_test_abi():
    return '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa


@pytest.fixture
def get_test_address():
    return '0x9326BFA02ADD2366b30bacB125260Af641031331'


# def test_rpc_url_not_present():
#     # Arrange
#     rpc_url = os.getenv('RPC_URL')
#     del os.environ['RPC_URL']

#     # Act / Assert
#     with pytest.raises(ValueError):
#         ChainlinkFeeds()

#     # reset
#     os.environ['RPC_URL'] = rpc_url


def test_get_latest_round_data():
    # Arrange
    network = 'kovan'
    pair = 'eth_usd'
    cf = ChainlinkFeeds(rpc_env_var='RPC_URL')

    # Act
    result = cf.get_latest_round_data(network=network, pair=pair)

    # Assert
    assert isinstance(result, dict)


def test_get_latest_round_data_with_abi_and_address(get_test_abi, get_test_address):
    # Arrange
    network = 'kovan'
    abi = get_test_abi
    address = get_test_address
    cf = ChainlinkFeeds(rpc_env_var='RPC_URL')

    # Act
    result = cf.get_latest_round_data(
        network=network, abi=abi, address=address)

    # Assert
    assert isinstance(result, dict)


def test_get_historical_price():
    # Arrange
    network = 'kovan'
    pair = 'eth_usd'
    round_id = 18446744073709556747
    cf = ChainlinkFeeds(rpc_env_var='RPC_URL')

    # Act
    result = cf.get_historical_price(round_id, network=network, pair=pair)

    # Assert
    assert isinstance(result, dict)


def test_load_config():
    # Arrange
    cf = ChainlinkFeeds(rpc_env_var='RPC_URL')

    # Act
    cf.load_config('./test/test_data/test_addresses_data.cfg',
                   abi_or_address='address')

    # Assert
    assert cf.get_manual_addresses(
    )['mainnet']['test_test'] == '0x0000000000000000000000000000000000000000'
