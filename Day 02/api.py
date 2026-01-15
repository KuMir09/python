import requests
import json

loc= "https://dog.ceo/api/breeds/list/all"

response = requests.get(url=loc)

# print(response.json())
# file = open("demo.json") # OPEN
# print(file.read()) # OPERATION
# # file.write(response.json())
# # file.close() # CLOSE


response_data = response.json()
print(response_data)
json_string = json.dumps(response_data, indent=4)

with open('demo.json', 'w') as file:
    file.write(json_string)

# print(dir(file))
# print(file.write.__doc__)