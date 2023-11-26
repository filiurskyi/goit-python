# aiowebserver.py
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def index_page(request):
    with open("index.html", "r") as f:
        html_text = f.read()
    response = web.Response(text=html_text, content_type="text/html")
    return response


def aiohttp_main():
    port = 5000
    app = web.Application()
    app.add_routes([web.get("/", index_page)])
    app.router.add_static("/", path="./", name="static")
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_main(), port=5000)
