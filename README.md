# chainlink_feeds

A way to pull data from the Chainlink Price Feeds for analytics, algorithmic trading models, or else

# Quickstart

```
from chainlink_feeds import ChainlinkFeeds

cf = ChainlinkFeeds(network='KOVAN', pari='ETH_USD')
print(cf.get_latest_round_data(network=network, pair=pair))
```
