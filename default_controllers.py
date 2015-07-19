import models.{PATH}
import controllers.main
import asyncio

@asyncio.coroutine
def delete(_id):
    yield from models.{PATH}.delete(_id)

@asyncio.coroutine
def show(_id):
    data = yield from models.{PATH}.show(_id)
    return data

@asyncio.coroutine
def show_all(**kwargs):
    data = yield from models.{PATH}.show_all(**kwargs)
    return data

@asyncio.coroutine
def update(_id, **kwargs):
    data = yield from models.{PATH}.update(_id, **kwargs)
    return data

@asyncio.coroutine
def create(**kwargs):
    data = yield from models.{PATH}.create(**kwargs)
    return data