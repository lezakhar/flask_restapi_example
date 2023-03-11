import requests
import json

url = 'http://127.0.0.1:5000'

# get all customers
endpoint = '/api/customers'
response = requests.get(url + endpoint)
print(response)
data = json.loads(response.text)
print(data)

# update 1 customer
endpoint = '/api/customers/1'
response = requests.put(url + endpoint, json={'Alina': 'Alina@mail.ru'})
print(response)

# check customers again
endpoint = '/api/customers'
response = requests.get(url + endpoint)
print(response)
data = json.loads(response.text)
print(data)
