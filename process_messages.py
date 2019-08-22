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
from person import Person


def get_group(response):
    '''
    Takes a dictionary response/GroupMe JSON as input
    Prompts user to choose which Groupme group they want to run script on
    It will return a single dictionary of the correct group
    '''
    # If only in 1 group, get it over with and return the group
    # Else, loop through, give the user an index to choose from
    response_size = len(response["response"])
    if  response_size == 1:
        return response["response"][0]
    else:
        print("You are in the following groups:")
        for i, groups in enumerate(response["response"], start=1):
            print(i, groups["name"])

    # Prompt user to select which group they wanna analyze from the groups 
    # they're in. If not in group, prompts them again.
    chosen = False
    while(not chosen):
        proper_group = int(input("What group, would you like to parse? "))
        if (chosen in range(0, response_size)):
            chosen = True
            print("\nGreat! Let's analyze:" \
                  f'{response["response"][proper_group-1]["name"]}')
        else:
            print(f"Uhm, '{proper_group}' that\'s not a proper response." \
                  "Try again chief.")

    return response["response"][proper_group-1]


def create_persons(group):
    '''
    Takes a dictionary JSON with just one group
    It will return a dict of initialized objects of each person in the group
    '''
    list_of_people = []
    dict_of_people_obj = {}

    for member in group["members"]:
        list_of_people.append(member["name"])

    # For each member create a Person object
    for person in group["members"]:
        new_person_obj = Person(person["id"], person["name"], 
                                person["image_url"], person["nickname"], 
                                list_of_people)

        dict_of_people_obj.update({new_person_obj.id: new_person_obj})

    return dict_of_people_obj


def process_message(people, msg_id):
    '''
    Recieves a dict of id/people key/value pairs and a message id
        it will call the API consecutively and return the last message_id?.. 
        and the updated dict of people.
    '''
    

def process_people(dict_people, group_id):
    '''
    Recieves a dict of id/people key/value pairs and processes each message 
        updating the object and processing each message.
    '''
    token = os.environ['MY_SECRET_TOKEN']
    limit = 100
    url = f'https://api.groupme.com/v3/groups/{group_id}/messages?token={token}&limit={limit}'
    response = requests.get(url)
    msg_json = json.loads(response.text)
    messages = msg_json["response"]["messages"] # Array of dicts
    last_message_id = messages[-1]["id"]

    print(json.dumps(msg_json, indent=2))

    count = msg_json["response"]["count"]
    print(last_message_id)
    print(count)
    print("The length of the messags: ", len(msg_json["response"]["messages"]))
    #msg_id =msg_json["response"]["messages"]["last_message_id"]
    

    done_processing = False
    while (not done_processing):
        proc_people, last_message_id, count = process_message(dict_people, msg_id)
        # Generate new msgid
        # Generate new count

    if count < 100:
        done_processing = True


    return {}



def main():
    # Be sure to add the token to .env, and you're in your pipenv
    token = os.environ['MY_SECRET_TOKEN']
    url = 'https://api.groupme.com/v3/groups?token=' + token
    response = requests.get(url)
    response_json = json.loads(response.text)


    # Parse the json to get the group
    group = response_json["response"][2] # Hard coded for now
    #group = get_group(response_json)
    people = create_persons(group)

    proc_people = process_people(people, group["group_id"])



if __name__ == '__main__':
    main()
