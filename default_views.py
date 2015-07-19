import asyncio
from urllib.parse import parse_qsl
from aiohttp import web
import controllers.{PATH}
import json

#GET
@asyncio.coroutine
def show_all(request):
    args = dict(parse_qsl(request._query_string))
    data = yield from controllers.{PATH}.show_all(**args)
    return web.Response(body=json.dumps(data).encode('utf-8'))

#GET
@asyncio.coroutine
def show(request):
    # args = dict(parse_qsl(request._query_string))
    data = yield from controllers.{PATH}.show(request._match_info['id'])
    return web.Response(body=json.dumps(data).encode('utf-8'))

#POST
@asyncio.coroutine
def delete(request):
    yield from controllers.{PATH}.delete(request._match_info['id'])

#POST
@asyncio.coroutine
def update(request):
    args = dict(parse_qsl(request._query_string))
    yield from controllers.{PATH}.update(request._match_info['id'], **args)

#POST
@asyncio.coroutine
def create(request):
    args = dict(parse_qsl(request._query_string))
    yield from controllers.{PATH}.create(**args)