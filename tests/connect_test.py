import pypyodbc
from pypika import Query, Table, Field
from rich import print
import pypyodbc


def test_always_true():
    assert True


def test_connect(fmdb):
    assert fmdb.cursor()


def test_select(fmdb: pypyodbc.Connection):
    cursor = fmdb.cursor()
    q = Query.from_("Products").select("Date", "Part Number")
    sql = q.get_sql()
    print(sql)
    results = cursor.execute(sql)
    all_results = results.fetchall()

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)
