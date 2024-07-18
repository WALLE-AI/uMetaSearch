import requests
import json
import time
import base64

request_url = "http://172.16.22.10:9000/WebAPI/QABot"

params = {"message":[
        {
        "content": "You are a helpful assistant",
        "role": "system"
        },
        {
        "content": '你能够做什么',
        "role": "user"
        }],}
headers = {'content-type': 'application/json'}
start = time.time()
response = requests.post(request_url, json=params, headers=headers)
print(response.json())








