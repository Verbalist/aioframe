from aioframe.models import Model
import psycopg2


def test_name_raw_query(db_Model):
    d = db_Model
    _c = d.query('select 1 as a', name='A2')
    assert _c.__class__.__name__ == 'A2'


def test_get_query_object_with_attr(db_Model):
    d = db_Model
    _c = d.query('select %s as vasa, %s as petya', (1, 'name'), name='A1')
    assert (_c.vasa, _c.petya) == (1, 'name')


def test_model_code_for_attr(db_Model):
    d = db_Model
    _c = d.query('select %s as vasa, %s as petya', (1, 'name'), name='A1')
    mod = __import__('tests.test_models.models', fromlist=['A1'])
    assert (mod.A1.petya, mod.A1.vasa) == (705, 23)


def test_get_cursor_with_close(db_Model):
    d = db_Model
    d.query('select 1')
    id_c = id(d.cursor)
    d.cursor.close()
    d.query('select 1')
    assert id_c != (id(d.cursor))
