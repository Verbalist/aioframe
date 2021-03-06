import asyncio
from aiopg.pool import create_pool

class PostgresStorage:
    """class for connect to db
    Attributes:
        config: dict with config to db connect"""

    def __init__(self, config):
        self.connection = None
        self.pool = None
        asyncio.wait([asyncio.async(self.connect(config))])

    # @async_log_critical_errors
    @asyncio.coroutine
    # @force_generator
    def connect(self, config):
        self.pool = yield from create_pool(user=config['user'], database=config['dbname'], password=config['password'],
                                           host=config['host'])
    @asyncio.coroutine
    # @force_generator
    def cursor(self):
        return (yield from self.pool.cursor())

    @asyncio.coroutine
    # @force_generator
    def execute(self, query, args=()):
        with (yield from self.cursor()) as cur:
            res = yield from cur.execute(query, args)

        return res

    @asyncio.coroutine
    # @force_generator
    def query(self, query, args=()):
        with (yield from self.cursor()) as cur:
            yield from cur.execute(query, args)
            rows = yield from cur.fetchall()

        return [{ cur.description[i].name : str(col) for i, col in enumerate(row) } for row in rows]

    @asyncio.coroutine
    def query_one(self, query, args=()):
        with (yield from self.cursor()) as cur:
            yield from cur.execute(query, args)
            row = yield from cur.fetchone()

        return { cur.description[i].name : str(col) for i, col in enumerate(row) }

    @asyncio.coroutine
    def mogrify(self, query, args=()):
        with (yield from self.cursor()) as cur:
            res = yield from cur.mogrify(query, args)
        return res
# @asyncio.coroutine
# def get_user(pool):
#     with (yield from pool.cursor()) as cur:
#         yield from cur.execute("SELECT * from trader where id = 7968", (yield))
#         ret = yield from cur.fetchone()

def get_db(path_to_config):
    db_config = {}
    with open(path_to_config, 'r') as config:
        for row in config:
            db_config[row.split('=')[0]] = row.split('=')[1].strip('\n')
    db = PostgresStorage(db_config)
    return db