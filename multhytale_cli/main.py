import typer

from .src.version import app as version_app
from .src.version import print_version_basic

app = typer.Typer(
    help="MultHytale: An easy to use multi-instance launcher for Hytale.",
    invoke_without_command=True,
    context_settings={
        "help_option_names": ["-h", "--help"],
    },
)

app.add_typer(version_app)


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Prints the version of the package.",
        is_eager=True,
    ),
):
    if version:
        print_version_basic()
        raise typer.Exit()

    if ctx.invoked_subcommand is None and not ctx.params["version"]:
        typer.echo(ctx.get_help())
        raise typer.Exit()
