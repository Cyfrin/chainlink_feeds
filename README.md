# chainlink_feeds

[![PyPI version](https://badge.fury.io/py/chainlink-feeds.svg)](https://badge.fury.io/py/chainlink-feeds.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/AlphaChainio/chainlink_feeds.svg)](http://isitmaintained.com/project/AlphaChainio/chainlink_feeds "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/AlphaChainio/chainlink_feeds.svg)](http://isitmaintained.com/project/AlphaChainio/chainlink_feeds "Percentage of issues still open")

A way to pull data from the Chainlink Price Feeds for analytics, algorithmic trading models, or else

# Quickstart

Install:

```
pip install chainlink_feeds
```

You'll need an `RPC_URL` environment variable.

```
from chainlink_feeds import ChainlinkFeeds

cf = ChainlinkFeeds()
print(cf.get_latest_round_data(network='KOVAN', pair='ETH_USD'))
```
