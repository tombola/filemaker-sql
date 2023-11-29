import pypyodbc
from pypika import Query, Tables
from rich import print
from fmsql.utils import select_all


def test_select_all(fmdb: pypyodbc.Connection):
    """
    https://www.databuzz.com.au/using-executesql-to-query-the-virtual-schemasystem-tables/
    """

    q = Query.from_("FileMaker_Tables").select("*")
    results = select_all(fmdb, q)

    assert isinstance(results, list)
