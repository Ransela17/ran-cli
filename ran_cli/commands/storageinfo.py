import click, json
from ran_cli.cli import Api


# --- Storage info Command --- #
@click.command()
def cli():
    """Returns storage summary information regarding binaries, file store and repositories"""
 
    endpoint='/storageinfo'
    response = Api.get_call(endpoint).json()
    click.echo(json.dumps(response, indent=4, sort_keys=True))
