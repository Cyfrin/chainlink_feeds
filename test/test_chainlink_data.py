# content of conftest.py
import pytest
import os

from ..chainlink_data import ChainlinkData


def test_rpc_url_not_present():
    # Arrange
    del os.environ['RPC_URL']

    # Act / Assert
    with pytest.raises(ValueError):
        ChainlinkData()


def test_get_latest_price():
    # Arrange
    network = 'KOVAN'
    pair = 'ETH_USD'

    # Act
    result =
    with pytest.raises(ValueError):
        ChainlinkData()
    # Assert
