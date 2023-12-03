# SPDX-FileCopyrightText: 2023-present tombola <tombola@github>
#
# SPDX-License-Identifier: MIT
import click

from fmsql.__about__ import __version__
from rich import print
from fmsql.settings import Settings


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="FileMaker SQL")
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["settings"] = Settings()


@cli.command()
@click.pass_context
def settings(ctx):
    print(ctx.obj["settings"])
