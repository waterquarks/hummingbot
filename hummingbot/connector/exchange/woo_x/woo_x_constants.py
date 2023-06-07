from hummingbot.core.api_throttler.data_types import RateLimit

DEFAULT_DOMAIN = "woo_x_main"

REST_URLS = {"woo_x_main": "https://api.woo.org/", "woo_x_staging": "https://api.staging.woo.org"}

SNAPSHOT_PATH_URL = '/v1/public/orderbook/'

RATE_LIMITS = [
    RateLimit(limit_id=SNAPSHOT_PATH_URL, limit=10, time_interval=1)
]

# Websocket event types
DIFF_EVENT_TYPE = "orderbookupdate"

TRADE_EVENT_TYPE = "trade"
