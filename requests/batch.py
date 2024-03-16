#!/usr/bin/python
import json
import requests

headers = {"Authorization": "Bearer token", "Content-type": "application/json"}
URL = "url"

# withfile = open("test.json", encoding="utf-8")
with open("test.json", encoding="utf-8") as file:

    data = json.load(file)

    for org in data:
        org_str = json.dumps(org)
        print(org_str)
        response = requests.post(URL, data=org_str, headers=headers, timeout=999)
        print(response.json())
