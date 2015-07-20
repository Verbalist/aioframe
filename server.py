import asyncio
from aiohttp import web, Response
# from aiohttp.server import ServerHttpProtocol
# from urllib.parse import urlparse, parse_qsl
# from aiohttp.multidict import MultiDict

# class HttpRequestHandler(ServerHttpProtocol):
#
#     @asyncio.coroutine
#     def handle_request(self, message, payload):
#         response = Response(
#             self.writer, 200, http_version=message.version
#         )
#         get_params = MultiDict(parse_qsl(urlparse(message.path).query))
#         print("Passed in GET", get_params)


app = web.Application()
loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, '0.0.0.0', 8080)
srv = loop.run_until_complete(f)
print('serving on', srv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.run_until_complete(app.finish())
loop.close()
