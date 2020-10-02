import requests

with open('../anu.txt') as fp:
    content = fp.read()

response = requests.post(
    'http://127.0.0.1:5000/uploads/2/iyaituom.txt', data=content
)

print(response.status_code)