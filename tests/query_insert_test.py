import pypyodbc
from pypika import Query, Tables
from rich import print

from fmsql.functions import FMDate


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
