# chainlink_feeds

[![PyPI version](https://badge.fury.io/py/chainlink-feeds.svg)](https://badge.fury.io/py/chainlink-feeds.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/AlphaChainio/chainlink_feeds.svg)](http://isitmaintained.com/project/AlphaChainio/chainlink_feeds "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/AlphaChainio/chainlink_feeds.svg)](http://isitmaintained.com/project/AlphaChainio/chainlink_feeds "Percentage of issues still open")
[![Actions Status](https://github.com/AlphaChainio/chainlink_feeds/workflows/chainlink_feeds/badge.svg)](https://github.com/workflows/chainlink_feeds/actions)

A way to pull data from the Chainlink Price Feeds for analytics, algorithmic trading models, or else.

This repo uses either an RPC_URL or the [Chainlink Subgraph](https://thegraph.com/explorer/subgraph/melonproject/chainlink)

# Quickstart

Install:

```
pip install chainlink_feeds
```

# Using the Chainlink subgraph

When you don't specify an RPC_URL, you automatically use the Chainlink subgraph.

```
from chainlink_feeds import ChainlinkFeeds

cf = ChainlinkFeeds()
print(cf.get_latest_round_data(pair='ETH_USD'))
```

You'll need an `RPC_URL` environment variable.

```
from chainlink_feeds import ChainlinkFeeds

cf = ChainlinkFeeds()
print(cf.get_latest_round_data(network='KOVAN', pair='ETH_USD'))
```

Result:

```
[{'assetPair': 'ETH/USD', 'blockHash': '0x141ad3c7468f4263d8b1b98a73f804b40ef1eb3a966bc2151646a08ba9872a58', 'blockNumber': '10887253', 'id': '0xf79d6afbb6da890132f9d7c355e3015f15f3406f/10887253/8', 'price': '38281000000', 'timestamp': '1600446952', 'transactionHash': '0x44e321f415e2ae236e3fbfb0df024825ff95331dca89dd25401303f0433fdb9d'}]
```

```
You can also pass:
cf.get_historical_price()
cf.get_price_feeds()
cf.get_prices()
cf.get_hourly_candle()
cf.get_daily_candle()
cf.get_weekly_candle()
```

This will get you all the data the subgraph can return. If you'd like to get pandas, you can just change the output format of the object.

```
cf = ChainlinkFeeds(output_format = 'pandas')
```
