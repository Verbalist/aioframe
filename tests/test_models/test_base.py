from aioframe.models import Model


def test_1(docker):
    import psycopg2

    container_ip = docker
    d = Model(psycopg2, {'database': 'test', 'user': 'test', 'host': container_ip, 'password': 'test'})
    _c = d.query('select %s as vasa, %s as petya', (1, 1), name='A1')
    print(_c)
    assert (_c.vasa, _c.petya) == (1, 1)
    assert _c.__class__.__name__ == 'A1'
    id_c = id(d.cursor)
    d.cursor.close()
    d.query('select 1 as vasa')
    assert id_c != (id(d.cursor))
