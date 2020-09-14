# content of conftest.py
import pytest
import os

from ..chainlink_feeds import ChainlinkFeeds


def test_rpc_url_not_present():
    # Arrange
    rpc_url = os.getenv('RPC_URL')
    del os.environ['RPC_URL']

    # Act / Assert
    with pytest.raises(ValueError):
        ChainlinkFeeds()

    # reset
    os.environ['RPC_URL'] = rpc_url


def test_get_latest_round_data():
    # Arrange
    network = 'KOVAN'
    pair = 'ETH_USD'
    cf = ChainlinkFeeds()

    # Act
    result = cf.get_latest_round_data(network=network, pair=pair)

    # Assert
    assert isinstance(result, dict)


def test_get_historical_price():
    # Arrange
    network = 'KOVAN'
    pair = 'ETH_USD'
    round_id = 50
    cf = ChainlinkFeeds()

    # Act
    result = cf.get_historical_price(round_id, network=network, pair=pair)

    # Assert
    assert isinstance(result, dict)
