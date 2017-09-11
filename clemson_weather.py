#!/bin/python
import requests
import json

# API endpoint for clemson memorial stadium
url = 'https://pickens.weatherstem.com/api'
# JSON request
indata = {'api_key':'abzbn5dl','stations':['clemson'], 'sensors': ['Thermometer']}


r = requests.post(url, data=json.dumps(indata))
data = json.loads(r.text)[0]

print (data["record"]["readings"][2]["value"])
