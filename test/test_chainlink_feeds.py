# content of conftest.py
import pytest
import logging as log
import pandas as pd

from ..chainlink_feeds import ChainlinkFeeds
log.basicConfig(level=log.INFO)


@pytest.fixture
def chainlink_feed():
    cf = ChainlinkFeeds()
    return cf


def test_convert_pair_format():
    # Arrange
    unconverted_pair = 'ETH_USD'

    # Act
    converted_pair = ChainlinkFeeds.convert_pair_format(unconverted_pair)

    # Assert
    assert converted_pair == 'ETH/USD'


def test_get_prices(chainlink_feed):
    # Arrange
    cf = chainlink_feed

    # Act
    result = cf.get_prices(pair='eth_usd')

    # Assert
    result[0]['assetPair'] == "ETH/USD"


def test_get_latest_round_data(chainlink_feed):
    # Arrange
    cf = chainlink_feed
    pair = 'eth_usd'

    # Act
    result = cf.get_latest_round_data(pair=pair)

    # Assert
    result[0]['assetPair'] == "ETH/USD"


def test_graphql_query(chainlink_feed):
    # Arrange
    cf = chainlink_feed
    query = """{
                    prices(where: {assetPair:"LINK/ETH"}, orderBy: timestamp, orderDirection:desc, first: 1000) {
                    id
                    price
                    timestamp
                    blockNumber
                    blockHash
                    transactionHash
                    assetPair
                    }
                }"""
    # Act
    result = cf.graphql_query(query)

    # Assert
    assert result['prices'][0]['assetPair'] == "LINK/ETH"


def test_pandas_output():
    # Arrange
    cf = ChainlinkFeeds(output_format='pandas')

    # Act
    result = cf.get_prices(pair='eth_usd')

    # Asset
    assert isinstance(result, pd.DataFrame)
    assert result['assetPair'][0] == 'ETH/USD'


def test_get_price_feeds(chainlink_feed):
    # Arrange
    cf = chainlink_feed

    # Act
    result = cf.get_price_feeds()

    # Assert
    assert isinstance(result[0]['assetPair'], str)


def test_get_hourly_candle(chainlink_feed):
    # Arrange
    cf = chainlink_feed

    # Act
    result = cf.get_hourly_candle(pair='ETH_USD')

    # Assert
    assert isinstance(result[0]['assetPair'], str)


def test_get_daily_candle(chainlink_feed):
    # Arrange
    cf = chainlink_feed

    # Act
    result = cf.get_daily_candle(pair='ETH_USD')

    # Assert
    assert isinstance(result[0]['assetPair'], str)


def test_get_weekly_candle(chainlink_feed):
    # Arrange
    cf = chainlink_feed

    # Act
    result = cf.get_weekly_candle(pair='ETH_USD')

    # Assert
    assert isinstance(result[0]['assetPair'], str)
