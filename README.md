# chainlink_feeds

A way to pull data from the Chainlink Price Feeds for analytics, algorithmic trading models, or else

# Quickstart

Install:

```
pip install chainlink_feeds
```

You'll need a `MNEMONIC` and `RPC_URL` environment variable.

```
from chainlink_feeds import ChainlinkFeeds

cf = ChainlinkFeeds(network='KOVAN', pari='ETH_USD')
print(cf.get_latest_round_data(network=network, pair=pair))
```
