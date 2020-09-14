# content of conftest.py
import pytest
import os

from ..chainlink_data import ChainlinkData


def test_rpc_url_not_present():
    """Raise an error with a bad RPC_URL
    """
    # Arrange
    del os.environ['RPC_URL']

    # Act / Assert
    with pytest.raises(ValueError):
        ChainlinkData()
