from db_connect import db
import models.main
import asyncio


@asyncio.coroutine
def show_all(limit=20, offset=0, sort='', **kwargs):
    data = yield from db.query("""
        SELECT * FROM {PATH} ORDER BY {0}
        limit %s offset %s""",
                               (limit, offset))
    return data

@asyncio.coroutine
def show(_id):
    data = yield from db.query("""
        SELECT * FROM {PATH} WHERE id = %s""",
                               (_id, ))
    return data

@asyncio.coroutine
def delete(_id):
    yield from db.execute("DELETE FROM {PATH} WHERE id = %s", (_id, ))

@asyncio.coroutine
def create(**kwargs):
    data = yield from db.query_one("insert into {PATH}("+','.join(list(kwargs.keys()))+") "
        "= ("+','.join(list(kwargs.keys()))+") returning *")
    return data

@asyncio.coroutine
def update(_id, **kwargs):
    data = yield from db.query_one("update {PATH} set ("+','.join(list(kwargs.keys()))+") "
        "= ("+','.join(list(kwargs.keys()))+") where id=%s returning *", (_id, ))
    return data