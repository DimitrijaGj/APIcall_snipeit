#! /usr/bin/env python

import json
from urllib import response
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# url of API source to retrive list of devices

url = "https://primeinfrasandbox.cisco.com/webacs/api/v3/data/Devices.json"

# Add the query parametar to indicate thet whole object be returned rather than just IDs of the entities
querystring = {".full": "true"}

# Provide login and password for the basic authorization

basicAuth = HTTPBasicAuth("devnetuser", "DevNet123!")

# Disable SSL certificate verification
ssl_verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Make request
response = requests.request(
    "GET", url, params=querystring, auth=basicAuth, verify=ssl_verify
)
print("====>")
print(response)

# Parse the recived JSON
parsed_response = json.loads(response.text)

# print("===>")
# print(parsed_response)

for entity in parsed_response["queryResponse"]["entity"]:
    ipAddress = entity["devicesDTO"]["ipAddress"]
    adminStatus = entity["devicesDTO"]["adminStatus"]
    # deviceType = entity["devicesDTO"]["deviceType"]
    deviceName = entity["devicesDTO"]["deviceName"]

    print(ipAddress, adminStatus, deviceName)
