import pypyodbc
import pytest


def get_dsn_connection_string(dsn="test", user="test", pwd=""):
    return f"DSN={dsn};UID={user};PWD={pwd}"


def get_connection_string():
    # TODO: get credentials from environment
    return "DRIVER={FileMaker ODBC};SERVER=localhost;DATABASE=inventory_test;UID=test;PWD="


@pytest.fixture
def fmdb():
    # TODO: this should return a singleton
    connection = pypyodbc.connect(connectString=get_connection_string())
    return connection
