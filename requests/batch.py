#!/usr/bin/python
import json
import requests

headers = {"Authorization": "Bearer token", 'Content-type': 'application/json'}
url  = 'url'

file = open('test.json')

data = json.load(file)

for org in data:
    org_str = json.dumps(org)
    print(org_str)
    response = requests.post(url, data=org_str, headers=headers)
    print(response.json())

file.close()