import pypyodbc
from pypika import Tables
from fmsql import FileMakerQuery as Query

from fmsql.dialects import FileMakerQuery as Query


def test_always_true():
    assert True


def test_connect(fmdb):
    assert fmdb.cursor()


def test_select(fmdb: pypyodbc.Connection):
    with fmdb:
        cursor = fmdb.cursor()
        q = Query.from_("Products").select("Date", "Part Number")
        sql = q.get_sql()
        print(sql)
        results = cursor.execute(sql)
        all_results = results.fetchall()

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)


def test_select_limit_offset(fmdb: pypyodbc.Connection):
    with fmdb:
        cursor = fmdb.cursor()
        q = Query.from_("Products").select("Date", "Part Number").limit(10)
        sql = q.get_sql()
        print(sql)
        results = cursor.execute(sql)
        all_results = results.fetchall()

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)
    assert len(all_results) == 10


def test_select_join(fmdb: pypyodbc.Connection):
    products, transactions = Tables("Products", "Inventory Transactions")
    with fmdb:
        cursor = fmdb.cursor()
        q = (
            Query.from_(products)
            .join(transactions)
            .on(products.PrimaryKey == transactions.ForeignKey)
            .select(products.Date, transactions.Units)
        )
        sql = q.get_sql()
        print(sql)
        results = cursor.execute(sql)
        all_results = results.fetchall()

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)
