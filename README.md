# Auto Create Remote Repo

With this script, you can automatically create a remote git repository.

# Pre-requisites
script takes a config file of format as shown below : 
~~~~
{
    "git_personal_token" :<Your git personal Token>,
    "user_git_api_url" : " https://api.github.com/graphql",
    "user_name" : <Your userName>
}
~~~~


# Usage

~~~~
C:\Users\E9968575\OneDrive - Eaton\Innovation\Experiments\Utils>python createGit.py -h
usage: createGit.py [-h] [-d REPODESC] [-a {PUBLIC,PRIVATE}] Name

Creation of Github Repo

positional arguments:
  Name                  Name of the repository to be created.

optional arguments:
  -h, --help            show this help message and exit
  -d REPODESC, --desc REPODESC
                        Description for the Repository
  -a {PUBLIC,PRIVATE}, --acc {PUBLIC,PRIVATE}
                        Access Level of the Repo to be created.
	
~~~~
