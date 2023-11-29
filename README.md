# filemaker-sql

Connect to FileMaker via odbc and run SQL queries against the FileMaker tables.

Uses PyPika query builder to simplify SQL construction.


Though `filemaker-sql`` should work cross platform, the constraints for my own use case were:

- Filemaker 18
- Mac OS


## Development requirements

- FileMaker installed
- libiodbc installed (`brew install libiodbc`)
- unixodbc uninstalled (`brew uninstall unixodbc`)
- `pre-commit install`