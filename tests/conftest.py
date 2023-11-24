import pytest
import pypyodbc


@pytest.fixture
def fmdb():
    dsn = "test"
    user = "test"
    pwd = ""
    connection_string = f"DSN={dsn};UID={user};PWD={pwd}"
    connection = pypyodbc.connect(connectString=connection_string)
    return connection
