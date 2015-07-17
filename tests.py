__author__ = 'verbalist'
import asyncio
from aiohttp import web, Response, server
from urllib.parse import urlparse, parse_qsl
import json

app = web.Application()

@asyncio.coroutine
def hello(request):
    print(request.__dict__)
    data = request._query_string
    params = parse_qsl(data)

    print(params)
    print({x[0]:x[1] for x in params})

    # print(parse_qsl(urlparse(request.path).__dict__))
    # print(parse_qsl(urlparse(request.path)).__dict__)
    # print(parse_qsl(urlparse(request.path).query))
    # print(request.match_info)
    data = json.dumps({x[0]:x[1] for x in params})
    return web.Response(body=data.encode('utf-8'))

app.router.add_route('GET', '/{name}', hello)
# app.router.add_route('GET', '/greet/{name}', handler.handle_greeting)

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
