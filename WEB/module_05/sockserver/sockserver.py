import asyncio
import json
import logging
from datetime import date, timedelta

import names
import websockets
from app import pb_api_getter
from websockets import WebSocketProtocolError, WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)


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
            msg = message.split()

            if msg[0] == "exchange" and len(msg) == 1:
                m = await self.get_currencies(1)
                await self.send_to_clients(m)
            elif msg[0] == "exchange" and msg[1].isnumeric():
                m = await self.get_currencies(int(msg[1]))
                await self.send_to_clients(f"Exchange rate:: \n{m}")
            else:
                await self.send_to_clients(f"{ws.name}: {message}")

    async def get_currencies(self, days=2):
        if days > 10:
            return "too much days, enter 10 or less"
        else:
            result = []
            for day in range(0, days):
                dt = date.today() - timedelta(days=day)
                data = await pb_api_getter(get_date=dt.strftime("%d.%m.%Y"))
                result.append(data)
        return json.dumps(result, indent=2)


async def run_socket():
    socket_server = SocketServer()
    async with websockets.serve(socket_server.ws_handler, "127.0.0.1", 8080):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(run_socket())
