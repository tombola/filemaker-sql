import pytest
import pypyodbc


def get_dsn_connection_string(dsn="test", user="test", pwd=""):
    return f"DSN={dsn};UID={user};PWD={pwd}"


def get_connection_string():
    return (
        "DRIVER={FileMaker ODBC};SERVER=localhost;DATABASE=inventory_test;UID=test;PWD="
    )


@pytest.fixture
def fmdb():
    connection = pypyodbc.connect(connectString=get_connection_string())
    return connection
