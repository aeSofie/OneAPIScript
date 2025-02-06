import os 
from dotenv import load_dotenv
import requests
import json

load_dotenv()

API_KEY_ID = os.getenv('API_KEY_ID')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')

#print(response.text)

def fetch_token(api_key_id, api_key_secret):
    url= 'https://api.apsis.one/oauth/token'
    header = {
        'Content-Type':'application/json'
    }
    payload = {
        'grant_type': 'client_credentials',
        'client_id' : api_key_id,
        'client_secret' : api_key_secret
    }
    response = requests.post(url=url, headers=header, json=payload)
    response_dict = json.loads(response.text)
    return response_dict

access_token = fetch_token(API_KEY_ID,API_KEY_SECRET)['access_token']

# print(access_token)

def fetch_keyspaces(access_token):
    url = 'https://api.apsis.one/audience/keyspaces'
    header = {
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url=url, headers=header)
    resp_dict = json.loads(response.text)

    return resp_dict

def fetch_sections(access_token):
    url = 'https://api.apsis.one/audience/sections'
    header = {
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url=url, headers=header)
    resp_dict = json.loads(response.text)

    return resp_dict

def fetch_attributes(access_token, section_disc):

    url = 'https://api.apsis.one/audience/sections/' + section_disc + '/attributes?include_keyspace_permissions=false'
    header = {
        'Authorization': 'Bearer ' + access_token
    }

    response = requests.get(url=url, headers=header)
    resp_dict = json.loads(response.text)

    return resp_dict

sections = fetch_sections(access_token)
attributes = fetch_attributes(access_token,'usercreated.sections.heartland_demo_2.0-rppfuhvt6a')

print(attributes)
