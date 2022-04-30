#! /usr/bin/env python

from wsgiref import headers
import requests
import json
from pprint import pprint

url = "https://it-inventory.trvapps.com/api/v1/locations/"

payload = {}

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiY2ExYTA5MDRlY2ZkZDg5MTlmMGU4MDBhMDRlNzZmOTc0Yjg3MGE0NTlkMmU2Y2I5NmZjNGQ4NGYyOWQzYTE1ZGI2N2JhMDYzZDgxNTU4NmQiLCJpYXQiOjE2NDk2NzczODAsIm5iZiI6MTY0OTY3NzM4MCwiZXhwIjoyOTExOTg0OTgwLCJzdWIiOiI0MDAwIiwic2NvcGVzIjpbXX0.xbs32y6xpdnS64JGuRLGHDfOinVQtb2C-i-m76kRCww1G3hlTfkumEMUQlEl5w8OWwhrTYHvn-rQLoiS701yvMHUlzxIaxWyZtF-b1Ekwzk0tU2b5KwpUNbqk0RFFypwIc-UEu0V5UO-MRUPYYEvXqNobSYntpZ6tSgzi49sfHbiGmwA3sqI6nwKq3gExRLxejUSfCIVOXJm5Mu_miKTcxUQeVe1ZzhG9lMjWdDT6Kze9aEGZin8oOpiuQLaSSWOzPXac5ler7OTSgwLhaOF_s1V72oIF_yoU39M_admnI5izdEqTTFLs0QSHk7_OQspcCzk0ev4sVObjfYwTKu93sTNos4JmrYk8erOwnFdcD8SvrP55pIOjeQlAolr2Ah1eT8ZxVgZqEbS-1rub_I33bJ0ODz1JTnc3qrSVGoJ_Wu2kp7jvu07h1gG9HiZm6eNyn-zichBgwHUBBXhxf1kMPwvwJ1hgsfD2Sf2cRdFFwAajSFmiBp5oQNeqki56erfERVe0T-qIipfP9FXO86e7bo60Kn4xu_8YSgn8s4DXfeSuZocbTMDPScvmqi63rb4Gv44ox2uv7PCCE96qSqgd2XDJvIUrqrrKvmY4tIbwmwb4OJYq7MnmaJTfPzad8IN-8F_DpeZltJyr9CKQu7CO6LRtfe6ZdLAcIE9Guc5meU",
    "Cookie": "XSRF-TOKEN=eyJpdiI6IlZJR3dGYkJ4ZXlOcDNRREUrWnNTcmc9PSIsInZhbHVlIjoibGhGSjAyV3h4ZjhJdUQ0cnlKZlplMkh4QU85b21pVnBQVzduSWptSVlqZ1BWVHNYYk5JejdMaXhiR3J3dytlbUVnbzVINzR3QmNieG1OWXZpeVpcL0tSNFJQaklMeTREaHFxODBYVCs3RmpueFwvdEZDclJhQjhUR21RelVLYjA4NiIsIm1hYyI6ImQ5NWEzMzRhODIxOTE1ZDZiZGQ2OThiZTg4Mjk3NzdhYzY2MWQwNTY5MzQxMDIxYmI5ODhlZWE0OGQ5ZjQxMjkifQ%3D%3D; snipeit_session=GkbhxcKGIJAQfNVpwGlyEGZr7huU2SxFzkpOBFDV",
    "Accept": "application/json",
}


response = requests.request("GET", url, headers=headers, data=payload)
parsed_response = json.loads(response.text)

if "rows" in parsed_response:
    if "id" in parsed_response["rows"]:
        print("JSON array")
        for sub in parsed_response["rows"]["id"]:
            print(sub)
