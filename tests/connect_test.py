import sqlalchemy
# for row in engine.execute('select * from aTable'): print (row)
# import sqlalchemy
# engine = sqlalchemy.create_engine('mysql+pypyodbc://MYSQL_ODBC_DSN') for row in engine.execute('select * from aTable'): print (row)

def test_always_true():
    assert True;

def test_connect():
    dsn = "test"
    user = "test"
    pwd = ""
    connection_string = f"DSN={dsn};UID={user};PWD={pwd}"
    engine = sqlalchemy.create_engine('mssql+pypyodbc://test')

    conn = engine.connect()
    # for row in engine.execute('select * from Products'): print (row)