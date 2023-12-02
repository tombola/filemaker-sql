# FileMaker SQL

[![PyPI - Version](https://img.shields.io/pypi/v/filemaker-sql.svg)](https://pypi.org/project/filemaker-sql)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/filemaker-sql.svg)](https://pypi.org/project/filemaker-sql)

Connect to FileMaker via odbc and run SQL queries against the FileMaker tables.

Uses PyPika query builder to simplify SQL construction.


Though `filemaker-sql`` should work cross platform, the constraints for my own use case were:

- Filemaker 18
- Mac OS


-----

**Table of Contents**

- [FileMaker SQL](#filemaker-sql)
  - [Installation](#installation)
  - [License](#license)
  - [Development requirements](#development-requirements)

## Installation

```console
pip install filemaker-sql
```

## License

`filemaker-sql` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


## Development requirements

- FileMaker desktop app
- libiodbc installed (`brew install libiodbc`)
- unixodbc uninstalled (`brew uninstall unixodbc`) _Hope to resolve this._
- `pre-commit install`