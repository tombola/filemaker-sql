import pytest
import pypyodbc


def get_connection_string():
    # dsn = "test"
    # user = "test"
    # pwd = ""
    # connection_string = f"DSN={dsn};UID={user};PWD={pwd}"
    return (
        "DRIVER={FileMaker ODBC};SERVER=localhost;DATABASE=inventory_test;UID=test;PWD="
    )


# brew uninstall --ignore-dependencies unixodbc && brew install libiodbc
@pytest.fixture
def fmdb():
    connection = pypyodbc.connect(connectString=get_connection_string())
    return connection


# NOT WORKING WITH PYODBC -
# import pyodbc

# Before re-testing:
# brew uninstall libiodbc && brew install unixodbc
# odbcinst -j
# cat /usr/local/etc/odbc.ini
# cat /usr/local/etc/odbcinst.ini
# @pytest.fixture
# def fmdb():
#     connection = pyodbc.connect(connectString=get_connection_string())
#     return connection
