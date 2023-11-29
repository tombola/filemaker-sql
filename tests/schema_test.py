import pypyodbc
from pypika import Query, Tables
from rich import print
from fmsql.functions import FMDate
from fmsql.utils import select_all


def test_fetch_tables(fmdb: pypyodbc.Connection):
    """
    https://www.databuzz.com.au/using-executesql-to-query-the-virtual-schemasystem-tables/
    """

    q = Query.from_("FileMaker_Tables").select("*")
    results = select_all(fmdb, q)

    assert isinstance(results, list)


def test_fetch_fields(fmdb: pypyodbc.Connection):
    """
    https://www.databuzz.com.au/using-executesql-to-query-the-virtual-schemasystem-tables/
    """
    with fmdb:
        cursor = fmdb.cursor()

        q = Query.from_("FileMaker_Fields").select("*")

        sql = q.get_sql()
        print(sql)
        results = cursor.execute(sql)
        all_results = results.fetchall()
        print(all_results)

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)
