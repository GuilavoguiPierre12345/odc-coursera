import requests

"""
url = "https://www.ibm.com/"

r = requests.get(url)
print(r.status_code)
header = r.request.headers
print(header['Accept-Encoding'])
print(r.encoding)
# print(r.request.body)

"""

url_get = "https://www.httpbin.org/get"
payload = {"name" : "Joseph", "ID": "123"}
response = requests.get(url_get, params=payload)
# print(response.request.headers)
print(response.json())