import asyncio
import json
from abc import ABC
from datetime import date, timedelta
from pprint import pprint

import aiohttp

currencies_interest = ["EUR", "USD"]

CURRENCIES = [
    "AUD",
    "AZN",
    "BYN",
    "CAD",
    "CHF",
    "CNY",
    "CZK",
    "DKK",
    "EUR",
    "GBP",
    "GEL",
    "HUF",
    "ILS",
    "JPY",
    "KZT",
    "MDL",
    "NOK",
    "PLN",
    "SEK",
    "SGD",
    "TMT",
    "TRY",
    "UAH",
    "USD",
    "UZS",
    "XAU",
]


class BaseCurrency(ABC):
    pass


class Currency(BaseCurrency):
    def __init__(self, single_currency: dict):
        self.name = single_currency["currency"]
        self.purchase_rate = single_currency["purchaseRateNB"]
        self.sell_rate = single_currency["saleRateNB"]


class CurrenciesAggregator:
    def __init__(self, currencies_json: str):
        self.currencies = {}
        currencies_json = json.loads(currencies_json)
        print(currencies_json)
        for currency in currencies_json["exchangeRate"]:
            self.currencies.update({Currency(currency).name: Currency(currency)})

    def get_all(self):
        return self.currencies

    def get_sale_purchase(self, curr_name: str):
        return {
            curr_name: {
                "sale": self.currencies.get(curr_name).sell_rate,
                "purchase": self.currencies.get(curr_name).purchase_rate,
            }
        }


async def pb_api_getter(get_date=date.today().strftime("%d.%m.%Y")):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.privatbank.ua/p24api/exchange_rates?json&date={get_date}"
        ) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])
            resp_json = await response.text()
            currencies_aggregator = CurrenciesAggregator(resp_json)
            out = {}
            for currency in currencies_interest:
                out.update(
                    {get_date: currencies_aggregator.get_sale_purchase(currency)}
                )
            return out


if __name__ == "__main__":
    asyncio.run(pb_api_getter())
