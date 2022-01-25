# importing required moduless
from getpass import getpass
import click, requests, os, configparser


__author__ = "Ran Sela"


#########
# Documentation for required libraries
#########
# https://click.palletsprojects.com/en/8.0.x/
# https://docs.python-requests.org/en/latest/
# https://docs.python.org/3/library/configparser.html
# https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API


config = configparser.ConfigParser()

my_headers = ''
repo_url = ''

try:
    config.read('config.ini')
    my_headers = {'X-JFrog-Art-Api' : config['jfrog']['apikey']}
    repo_url = config['jfrog']['url']
except:
    pass


#########
# MyCLI Class - Custom Multi Commands - From Click Library
#########
plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')


#########
# Api Class - Requests Calls To Jfrog Artifactory 
#########
class Api(object):
    
    def __init__(self):
        pass
    
    def get_call(endpoint):
        jfrog = requests.get(repo_url + endpoint, headers=my_headers)
        
        return (jfrog)
    
    def post_call(endpoint, data):
        jfrog = requests.post(repo_url + endpoint, headers=my_headers, json=data)

        return (jfrog)

    def put_call(endpoint, data):
        jfrog = requests.put(repo_url + endpoint, headers=my_headers, json=data)
       
        return (jfrog)

    def delete_call(endpoint):
        jfrog = requests.delete(repo_url + endpoint, headers=my_headers)
        
        return (jfrog.text)


#########
# JfrogAuth Class -  Jfrog Artifactory 
#########

MAX_CREDETIALS_TRIES = 3

class jfrogAuth():

    def __init__(self):
        pass

    # Login, checks the user input a maximum of 3 attempts, otherwise need to write 'ran' command again    
    def login(self):

        if self.configExists(): 
            return True
        
        for times in range(MAX_CREDETIALS_TRIES):
            print('')
            server = input("Enter Artifactory Server Name: ")
            user = input("Enter Email: ")
            password = getpass()
            if (self.verify_connection(server,user,password)):
                return True

        return False
    
    # Create a config file
    def createConfing(self, repo_url, reposnse):
        config['jfrog'] = {
            'url': repo_url,
            'apikey': reposnse
        }

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
        return True
    
    # Check if config.ini file is exists
    def configExists(self): 
        configfile = 'config.ini'
        if os.path.isfile(configfile) and os.path.getsize(configfile) != 0:
            return True

        return False    
    
    # Checks if the user information are correct by making api call to Jfrog Artifactory,
    # if correct, a conifg file has been created
    def verify_connection(self, server, user, password):
        global my_headers, repo_url
        endpoint = '/security/apiKey'
        repo_url = 'https://' + server + '.jfrog.io/artifactory/api'
        try:    
            reposnse = requests.get(repo_url+endpoint, auth=(user, password))
            if (reposnse.status_code > 200):
                click.echo('Incorrect credentials. Please try again.')
                return False
                
            reposnse = reposnse.json()    
            if not 'apiKey' in reposnse:
                click.echo('You Most Generate API Key Before Using the CLI - Get into Jfrog Platform >> Edit Profile >> Authentication Settings')
                return False

            my_headers = {'X-JFrog-Art-Api' : reposnse['apikey']}
            self.createConfing(repo_url, reposnse['apiKey'])

        except:
            click.echo('Could not request to jfrog server. Check your credentials and try again.')
            return False

        return True
     
   
#########
# ran Command Line Interface
#########
@click.command(cls=MyCLI)
def cli():
    """
    Simple CLI to manage an Artifactory SaaS instance via its API
    """
    j = jfrogAuth()
    if not j.login():
        exit()

                