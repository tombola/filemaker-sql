# SPDX-FileCopyrightText: 2023-present tombola <tombola@github>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from filemaker_sql.cli import filemaker_sql

    sys.exit(filemaker_sql())
