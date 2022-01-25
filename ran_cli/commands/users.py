
import click
from ran_cli.cli import Api

# --- User Group command called users  --- #
@click.group()
def cli():
    """Several commands to make operations on Jfrog Artifactory users"""
    pass

# --- Create user command --- #
@cli.command()
@click.option('-u', '--user', type=str, required=True)
@click.option('-e', '--email', type=str, required=True)
@click.option('-p', '--password', help='Required most contain at least 8 characters, at least 1 uppercase and lowercase', required=True)
@click.option('-a', '--admin', type=bool, default=False, show_default=True)
@click.option('-pu','--profileUpdatable', type=bool, default=True, show_default=True)
@click.option('-dui','--disableUIAccess', type=bool, default=True, show_default=True)
@click.option('-ipd','--internalPasswordDisabled', type=bool, default=False, show_default=True)
@click.option('-g','--groups')
def create(user,email,password, admin, profileupdatable, disableuiaccess, internalpassworddisabled, groups):
    """Creates a new user in Artifactory or replaces an existing user"""

    endpoint = '/security/users/'+user
    data = {
        'name': user,
        'email': email,
        'password': password,
        'profileUpdatable': profileupdatable,
        'disableUIAccess': disableuiaccess,
        'internalPasswordDisabled': internalpassworddisabled,
        'groups': groups
    }
    response = Api.put_call(endpoint, data)
    click.echo(response.text)


# --- Delete user command --- #
@cli.command()
@click.option('-u','--user', type=str, help='Required - Provide user name ', required=True, prompt_required=False)
@click.confirmation_option(prompt='Are you sure you want to delete user?')
def delete(user):
    """Removes an Artifactory user"""

    endpoint = '/security/users/'+user
    response = Api.delete_call(endpoint)
    click.echo(response)


