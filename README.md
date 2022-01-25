# Ran
ran is a cli tool to bring together all my utilities into a centralised place.


## How to Install
1. `git clone `
2. `pip install `
3. `eve [cmd]` See [Examples](#Examples) section for commands to run.`

## Documentation for required libraries

- https://click.palletsprojects.com/en/8.0.x/
- https://docs.python-requests.org/en/latest/
- https://docs.python.org/3/library/configparser.html
- https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API

## Examples for 'ran' commands 

```commandline
Usage: ran [OPTIONS] COMMAND [ARGS]...

  Simple CLI to manage an Artifactory SaaS instance via its API

Options:
  --help  Show this message and exit.

Commands:
  ping         'Get a simple status response about the state of Artifactory'
  repo         Several commands to make operations on Jfrog Artifacts...
  storageinfo  Returns storage summary information regarding binaries,...
  users        Several commands to make operations on Jfrog Artifactory...
  version      Retrieve information about the current Artifactory version'
  ```

```commandline
$ ran version

Artifactory Version is: 7.31.10

```

```commandline
$ ran users create --help

Usage: ran users create [OPTIONS]

  Creates a new user in Artifactory or replaces an existing user

Options:
  -u, --user TEXT                 [required]
  -e, --email TEXT                [required]
  -p, --password TEXT             Required most contain at least 8 characters,
                                  at least 1 uppercase and lowercase
                                  [required]
  -a, --admin BOOLEAN             [default: False]
  -pu, --profileUpdatable BOOLEAN
                                  [default: True]
  -dui, --disableUIAccess BOOLEAN
                                  [default: True]
  -ipd, --internalPasswordDisabled BOOLEAN
                                  [default: False]
  -g, --groups TEXT
  --help                          Show this message and exit.

```

```commandline
$ ran repo list --help
Usage: ran repo list [OPTIONS]

  Returns a list of minimal repository details for all repositories of the
  specified type

Options:
  -t, --type [local|remote|virtual|distribution]
                                  Most Provide the Type from the list:
                                  local|remote|virtual|distribution
                                  [required]
  -pt, --packageType [maven|gradle|ivy|sbt|helm|cocoapods|opkg|rpm|nuget|cran|gems|npm|bower|debian|composer|pypi|docker|vagrant|gitlfs|go|yum|conan|chef|puppet|generic|]
                                  Choose one of the following: maven|gradle|iv
                                  y|sbt|helm|cocoapods|opkg|rpm|nuget|cran|gem
                                  s|npm|bower|debian|composer|pypi|docker|vagr
                                  ant|gitlfs|go|yum|conan|chef|puppet|generic
  --help                          Show this message and exit.

```

