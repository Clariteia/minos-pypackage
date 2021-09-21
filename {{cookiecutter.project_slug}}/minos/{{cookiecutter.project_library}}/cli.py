{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
import typer
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "minos.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "minos.cli.main")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
app = typer.Typer()

@app.command("start")
def start():
    """Perform Start operation."""

    raise NotImplementedError


@app.command("status")
def status():
    """Perform Status operation."""
    raise NotImplementedError


@app.command("stop")
def stop():
    """Perform Stop operation."""
    raise NotImplementedError
{%- endif %}

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
