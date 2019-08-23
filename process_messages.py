'''
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

TOKEN= os.environ['MY_SECRET_TOKEN']

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
    # they're in. If input not in group, prompt again.
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

    # Create list of strings to pass and create People objects later
    for member in group["members"]:
        list_of_people.append(member["name"])

    # For each member create a Person object and append to dict
    for person in group["members"]:
        new_person_obj = Person(person["id"], person["name"], 
                                person["image_url"], person["nickname"], 
                                list_of_people)
        dict_of_people_obj.update({new_person_obj.id: new_person_obj})

    return dict_of_people_obj


def process_message(messages, people):
    '''
    Recieves a dict of id/people key/value pairs and a message id
        it will call the API consecutively and mutate the dict of 
        people, incrementing the necessary fields.
    '''
    #for msg in messages:
        #print(json.dumps(msg, indent=2))
    

def process_people(dict_people, group_id):
    '''
    Recieves a dict of id/people key/value pairs and processes each message 
        updating the object and processing each message.
    '''
    # Create URL
    limit = 100
    url = f'https://api.groupme.com/v3/groups/{group_id}/messages?token={TOKEN}&limit={limit}'
    response = requests.get(url)
    msg_json = json.loads(response.text)
    messages = msg_json["response"]["messages"] # List of dicts
    last_message_id = messages[-1]["id"]
    count = msg_json["response"]["count"]

    print("The length of the messags: ", len(messages))
    
    # Loop through all of the messages in the API call
    done_processing = False
    while (not done_processing):
        print("Parsing... messages left:",count)
        if count <= 100:
            done_processing = True
            process_message(messages, dict_people)
            break

        process_message(messages, dict_people)

        # Create URL again anew
        url = f'https://api.groupme.com/v3/groups/{group_id}/messages?token='\
              f'{TOKEN}&limit={limit}&before_id={last_message_id}'
        print("THE FUCKKING URL IS",url)
        print("You SUCK JUST QUIT BITCH")
        response = requests.get(url)
        msg_json = json.loads(response.text)
        messages = msg_json["response"]["messages"] # List of dicts
        last_message_id = messages[-1]["id"]
        count = count - len(messages)


    return dict_people



def main():
    # Be sure to add the token to .env, and you're in your pipenv
    url = f'https://api.groupme.com/v3/groups?token={TOKEN}'
    response = requests.get(url)
    response_json = json.loads(response.text)

    # Parse the json to get the group
    group = get_group(response_json)
    people = create_persons(group)
    proc_people = process_people(people, group["group_id"])

    print("\n\n**************************") 
    print("PRINTING VALUE OF PROCESSED PPL")
    for bitch in proc_people.values():
        print(bitch)

    print("\n\n**************************") 

if __name__ == '__main__':
    main()
