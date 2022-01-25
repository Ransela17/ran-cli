import click
from ran_cli.cli import Api


# --- Version Command --- #
@click.command()
def cli():
    """Retrieve information about the current Artifactory version'"""
   
    endpoint ='/system/version'
    response = Api.get_call(endpoint).json() # Get the json format
    version = response['version'] # Get only the vesion number
    click.echo('\n''Artifactory Version is: ' + version + '\n')
    pass