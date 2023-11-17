import aiohttp
import asyncio


async def api_getter(date="17.11.2023"):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            received_json = await response.text()
            print(received_json)


if __name__ == "__main__":
    asyncio.run(api_getter())
