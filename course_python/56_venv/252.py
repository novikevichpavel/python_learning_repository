import requests
import json

my_req = requests.get("https://api-test6-11.emall.by/")

print(my_req)
response = my_req.text
print(response)
print(my_req.status_code)