# filemaker-sqlalchemy
Proof of Concept for connecting to FileMaker database using via an ORM ([background](https://github.com/vitalseeds/vs-data-api/issues/4#issuecomment-1436095032)).
ORM selected is SQL Alchemy, as this is widely used and documented. If I can get that working I would like to use [SQLmodel](https://sqlmodel.tiangolo.com/).
A fallback would at least be to allow use with SQL core to simplify SQL construction.

The constraints for my use case are:

- Filemaker 18
- Mac OS

## Challenges

- SQL Alchemy uses pyodbc
    - pyodbc uses unixdb library for odbc connection
    - Filemaker (on mac anyway) uses IODBC library

Options: compile pyodbc with links to iodbc _OR_ get SQL alchemy to use pypyodbc

1. SQL Alchemy does not the same SQL syntax as FileMaker
2. Filemaker only supports a subset of SQL

Options:
1.Create an SQL Alchemy dialect that adapts the SQL syntax used
    - probably based off the mssql dialect, which also uses pyodbc
2. If SQLalchemy cannot work without this subset, this may all be a dead end\*

----
\* eg I noticed that FM does not support SQL `LIMIT` 🤦


## Setup

I avoided submodules for this so just cloning my sqlalchemy fork into the test directory

`git clone --depth 1 --branch add-pypyodbc git@github.com:tombola/sqlalchemy.git`

Setup a virtual environment.

`pyenv virtualenv 3.11 fmsql-3.11 && echo fmsql-3.11 > .python-version`

`pip install -e ./sqlalchemy`
`pip install -r requirements.txt`