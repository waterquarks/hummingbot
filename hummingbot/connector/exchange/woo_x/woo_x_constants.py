from hummingbot.core.api_throttler.data_types import RateLimit

DEFAULT_DOMAIN = "woo_x"

REST_URLS = {
    "woo_x": "https://api.woo.org/",
    "woo_x_staging": "https://api.staging.woo.org"
}

WSS_PUBLIC_URLS = {
    "woo_x": "wss://wss.woo.org/ws/stream/ff7607b9-8ca6-4540-b5b2-b8efee350a49",
    "woo_x_staging": "wss://wss.staging.woo.org/ws/stream/6a9b8f2b-3969-4c96-b127-b6649b7d976d"
}

WSS_PRIVATE_URLS = {
    "woo_x": "wss://wss.woo.org/ws/stream/ff7607b9-8ca6-4540-b5b2-b8efee350a49",
    "woo_x_staging": "wss://wss.staging.woo.org/v2/ws/private/stream/6a9b8f2b-3969-4c96-b127-b6649b7d976d"
}

WS_HEARTBEAT_TIME_INTERVAL = 30

SNAPSHOT_PATH_URL = '/v1/public/orderbook/'
ORDER_PATH_URL = '/v1/order'
MY_TRADES_PATH_URL = '/v1/client/trades'

RATE_LIMITS = [
    RateLimit(limit_id=SNAPSHOT_PATH_URL, limit=10, time_interval=1)
]

# Websocket event types
DIFF_EVENT_TYPE = "orderbookupdate"
TRADE_EVENT_TYPE = "trade"

SECONDS_TO_WAIT_TO_RECEIVE_MESSAGE = 20  # According to the documentation this has to be less than 30 seconds

