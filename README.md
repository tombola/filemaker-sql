# filemaker-sqlalchemy
Proof of Concept for connecting to FileMaker database using via an ORM
([background](https://github.com/vitalseeds/vs-data-api/issues/4#issuecomment-1436095032)),
or at least rationalising ODBC connection code with a query builder.

ORM initially selected was SQL Alchemy, as this is widely used and documented. If I can get that working I would like to use [SQLmodel](https://sqlmodel.tiangolo.com/).
A fallback would at least be to allow use with SQL core to simplify SQL construction.

The constraints for my use case are:

- Filemaker 18
- Mac OS