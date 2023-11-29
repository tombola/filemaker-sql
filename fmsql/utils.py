import pypyodbc
from pypika import Query, Tables


def select_all(fmdb: pypyodbc.Connection, query):
    with fmdb:
        cursor = fmdb.cursor()
        sql = query.get_sql()
        print(sql)
        results = cursor.execute(sql)
        if results:
            return results.fetchall()
