from urls import url
from aiohttp import web
import asyncio
import json
import controllers.{PATH}

@asyncio.coroutine
def main(request):
    _query_string = yield from request._query_string


    response = json.dumps()
    return web.Response(body = controllers.{PATH}.get_all())


urlpatterns = [url('GET',r'/{PATH}', views.{PATH}.main),
               url('GET',r'/{PATH}update/{id}', views.{PATH}.update),
               url('GET',r'/{PATH}create/{id}', views.{PATH}.create),
               url('GET',r'/{PATH}delete/{id}', views.{PATH}.delete),
               url('GET',r'/{PATH}show/{id}', views.{PATH}.show)]
