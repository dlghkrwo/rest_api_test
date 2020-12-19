import requests
import json
import jsonpath


# how i can fetch the body and header, how i can send get request through api url
#how i can make jsonpath to fetch response content. and when everything is ok, i'm able to compared actual result and expect result
#also delete the request, and post data with json file

# api url
url = "https://reqres.in/api/users?page=2"

# send Get request
response = requests.get(url)

# display response content
# print(response.content)
# print(response.headers)

# parse response to Json format
json_response = json.loads(response.text)
#print(json_response)

# fetch value using Json path.  whenever we are applying jsonpath to any response it will return a list
# and list can have any number of items
pages = jsonpath.jsonpath(json_response, 'per_page')
assert pages[0] == 6
