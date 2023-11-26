# main.py
import asyncio

import websockets
from aiohttp import web
from aiowebserver import aiohttp_main
from sockserver import SocketServer, run_socket


async def main_sock():
    socket_server = SocketServer()

    sock_server = websockets.serve(socket_server.ws_handler, "localhost", 8081)
    return sock_server.ws_server


async def main_web():
    app = aiohttp_main()
    web.run_app(app)


# def main():
#     socket_server = SocketServer()
#     sock_app = websockets.serve(socket_server.ws_handler, "localhost", 8081)
#     return


#
#     # ==== normal http ====
#     # server_address = ("localhost", 3000)
#     # http = HTTPServer(server_address, HttpHandler)
#
#     # ==== aiohttp ====
#     site = await aiohttp_main()
#     print(type(site))


async def main():
    sock_task = await main_sock()
    tasks = [main_web]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
