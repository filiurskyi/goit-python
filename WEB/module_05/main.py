import asyncio
import logging

import aiohttp
import names
import websockets
from webserver import run_web
from websockets import WebSocketProtocolError, WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)

async def get_exchange():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        ) as resp:
            if resp.status == 200:
                r = await resp.json()
                (exc,) = list(filter(lambda el: el["ccy"] == "USD", r))
            return f"USD: buy: {exc['buy']}, sale: {exc['sale']}"




class SocketServer:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects")

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects")

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except WebSocketProtocolError as err:
            logging.error(err)
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if message == "exchange":
                m = await get_exchange()
                await self.send_to_clients(m)
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def run_socket():
    socket_server = SocketServer()
    async with websockets.serve(socket_server.ws_handler, "localhost", 8085):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(run_socket())
    asyncio.run(run_web())
