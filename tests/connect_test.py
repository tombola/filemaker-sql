import pypyodbc
from pypika import Query, Tables
from rich import print
from fmsql.functions import FMDate


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


def test_select_join(fmdb: pypyodbc.Connection):
    products, transactions = Tables("Products", "Inventory Transactions")
    with fmdb:
        cursor = fmdb.cursor()
        q = (
            Query.from_(products)
            .join(transactions)
            .on(products.pk == transactions.fk)
            .select(products.Date, transactions.Units)
        )
        sql = q.get_sql()
        print(sql)
        results = cursor.execute(sql)
        all_results = results.fetchall()

    assert isinstance(results, pypyodbc.Cursor)
    assert isinstance(all_results, list)


def test_insert(fmdb: pypyodbc.Connection):
    products, transactions = Tables("Products", "Inventory Transactions")
    with fmdb:
        cursor = fmdb.cursor()
        columns = (
            "Name",
            "Category",
            "Part Number",
            "Date",
            "Location",
            "Unit Price",
            "Unit Price",
        )
        from pypika.functions import Convert

        q = (
            Query.into(products)
            .columns(*columns)
            .insert(
                "Box",
                "Vessel",
                "125",
                FMDate(),
                "Cupboard",
                10,
                12,
            )
        )

        sql = q.get_sql()
        print(sql)
        result = cursor.execute(sql)
        # all_results = results.fetchall()
    print(result)
    assert result
    # assert isinstance(results, pypyodbc.Cursor)
    # assert isinstance(all_results, list)
