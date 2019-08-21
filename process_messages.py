'''
USEFUL PYTHON MODULES FOR G-MO
[x] requests
[x] json
[x] csv

CHECKLIST
[x] make a groupme_person class with properties: likes_given, likes_received, #_of_messages, anything else?
[x] call the API to get the correct group and initialize people for all the people in the group
[]   ----> problem with Emmett where he left the group but also gave out likes, how to handle?
[] query for messages until you reach the beginning
[] while querying, loop through the messages and increment relevant properties on relevant messages
[] print out the stats to a csv file to be used for data visualization


[x]how to set the access token to an environment variable?
[x]how to modularize searching for a group? (ask for user input?) how to modularize groupme access token? (probably not)

# this is to ignore the ssl insecure warning as we are passing in 'verify=false'
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy is needed if running on Intel network
http_proxy  = "http://proxy-us.intel.com:911"
https_proxy = "https://proxy-us.intel.com:911"
ftp_proxy   = "ftp://proxy-us.intel.com:911"

proxyDict = { 
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }
response = requests.get(url, verify=False, proxies=proxyDict)
'''

import json
import requests
import urllib3
import os
from Person import Person


def get_group(response):
    '''
    Takes a dictionary response/GroupMe JSON as input. This is a list of dictionaries.
    Prompts user to choose which Groupme group they want to run script on.
    It will return a single dictionary of the correct group.
    '''
    # If only in 1 group, get it over with and return the group
    if len(response["response"]) <= 1:
        return response["response"][0]
    else:
        print("You are in the following groups:")
        for i, groups in enumerate(response["response"], start=1):
            print(i, groups["name"])


    proper_group = int(input("What group, would you like to parse? "))

    return response["response"][proper_group-1]


def create_persons(group):
    '''
    Takes a dictionary JSON with just one group.
    It will return a list of initialized objects of each person in the group.
    '''
    list_of_people = []

    for person in group["members"]:
        new_person_obj = Person(person["id"], person["name"], person["image_url"], person["nickname"])
        list_of_people.append(new_person_obj)

    return list_of_people


def process_message():
    pass

def process_people():
    pass

def main():
    # Be sure to add the token to .env
    token = os.environ['MY_SECRET_TOKEN']
    url = 'https://api.groupme.com/v3/groups?token=' + token
    response = requests.get(url)
    response_json = json.loads(response.text)


    # Parse the json to get the group
    group = response_json["response"][2]
    #group = get_group(response_json)
    people = create_persons(group)

    print(type(people))
    print(people)



if __name__ == '__main__':
    main()
