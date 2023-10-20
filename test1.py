import requests
import json

APIURL = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
response = requests.get(APIURL)

def get_jsondata():
    list_account = []
    for data in response.json()['items']:
        #print("results is:", data['title'])
        list_account.append(data['owner']['account_id'])
    print("Created list:", list_account)

get_jsondata()
