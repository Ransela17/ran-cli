import click, json
from ran_cli.cli import Api


# --- Ping Command --- #
@click.command()
def cli():
    """'Get a simple status response about the state of Artifactory'"""

    endpoint='/system/ping'
    click.echo('\n' + Api.get_call(endpoint).text +'\n') 
