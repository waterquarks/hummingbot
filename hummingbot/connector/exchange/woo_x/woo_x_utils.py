from decimal import Decimal

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True

EXAMPLE_PAIR = "BTC-USDT"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.001"),
    taker_percent_fee_decimal=Decimal("0.001"),
)


class WooXConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="woo_x", const=True, client_data=None)
    public_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Woo X public API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    secret_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Woo X secret API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    application_id: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Woo X application ID",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = "woo_x"


KEYS = WooXConfigMap.construct()
