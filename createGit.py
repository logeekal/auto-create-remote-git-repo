#!/usr/bin/env python

import sys
import requests
import json
import base64
import argparse


parser =  argparse.ArgumentParser(description="Creation of Github Repo")


parser.add_argument("Name", help="Name of the repository to be created.")
parser.add_argument("-d","--desc",nargs=1, help="Description for the Repository",dest="repoDesc")
parser.add_argument("-a","--acc",action="store",nargs=1, choices=['PUBLIC','PRIVATE'], default='PRIVATE', help="Access Level of the Repo to be created.", dest="repoAccess")

args = parser.parse_args()
print(args)
repoName = args.Name
if(args.repoDesc != None):
    repoDesc = args.repoDesc[0]
else:
    repoDesc ='PRIVATE'
repoAccess = args.repoAccess



with open('./config.json','r') as f:
    config = json.load(f)

#PROXY ="http://proxy.etn.com:8080"
PROXY= ""

GIT_PTOKEN = config['git_personal_token'];
USER_GIT_URL =  config['user_git_api_url'];
USER_NAME =  config['user_name']
PROXY = {
    "http" :PROXY,
    "https":PROXY
}


AUTH_HEADER = {"Authorization" : "bearer %s" % GIT_PTOKEN}


def getTemplateRepoId ():
    """This gets my  owner id from my github profile as it is a mandatory attribute for creating a repo."""
    query = """{
   repository(owner:"logeekal", name:"Generic_template"){
       id
   }
    }"""

    response = requests.post(USER_GIT_URL, headers=AUTH_HEADER, json={"query" : query}, proxies=PROXY )

    return response.json()['data']['repository']['id']
    
def getOwnerID():
    """This gets my  owner id from my github profile as it is a mandatory attribute for creating a repo."""
    query = """
    {
        user(login:"logeekal"){
            id
        }
    }
    """

    response = requests.post(USER_GIT_URL, headers=AUTH_HEADER, json={"query": query}, proxies=PROXY);

    return response.json()["data"]["user"]["id"]


def createRepo(repoName, repoDesc, repoAccess="PRIVATE"):
    templateId = getTemplateRepoId()
    print("Template Id is  : %s" % templateId)
    ownerId = getOwnerID()
    print("User Id is  : %s" % ownerId)

    print('%s \n %s \n %s' % (repoName, repoDesc, repoAccess))

    if((repoDesc == "") or (repoDesc == None)):
        repoDesc = repoName

    repoCreateMutation = """
                mutation {
            cloneTemplateRepository(input:{
                name : \"%s\",
                description : \"%s\"
                visibility :  %s
                repositoryId : \"%s\",
                ownerId:\"%s\"
            }){
                clientMutationId
                repository{
                    name
                        
                }
            }
        }
    """ % (repoName, repoDesc, repoAccess, templateId, ownerId)

    print(repoCreateMutation);

    response =  response = requests.post(USER_GIT_URL, headers=AUTH_HEADER, json={"query": repoCreateMutation}, proxies=PROXY);
    print(response.json())
    if(response.json()['data']['cloneTemplateRepository']['repository']['name'] == repoName):
        print('Remote Repository %s uccessfully created. Now cloning it.' % repoName)



createRepo(repoName, repoDesc, repoAccess);

