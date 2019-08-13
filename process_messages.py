'''
USEFUL PYTHON MODULES FOR G-MO
- requests
- json
- csv

- make a groupme_person class with properties: likes_given, likes_received, #_of_messages, anything else?
- call the API to get the correct group and initialize people for all the people in the group
----> problem with Emmett where he left the group but also gave out likes, how to handle?
- query for messages until you reach the beginning
- while querying, loop through the messages and increment relevant properties on relevant messages
- print out the stats to a csv file to be used for data visualization


how to set the access token to an environment variable?
Create a .env file and name your token: ''Enviroment Variable
how to modularize searching for a group? (ask for user input?) how to modularize groupme access token? (probably not)
'''
import json
import requests
import urllib3
import os

# this is to ignore the ssl insecure warning as we are passing in 'verify=false'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = os.environ['MY_SECRET_TOKEN']
url = 'https://api.groupme.com/v3/groups?token=' + token

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
response = requests.get(url)


print(json.loads(response.text))
