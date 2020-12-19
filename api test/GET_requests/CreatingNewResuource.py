import requests
import json
import jsonpath

#read input json from file and parse into json format and hit post method and parse response to json format
# and validating response

# api url
url = "https://reqres.in/api/users"

#read input json file
file = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\creatingUser.json', 'r') # read the file
json_input = file.read() #reading the file from the content and store in the variable
request_json = json.loads(json_input) #loads will do parse the data into json format


#make POST request with Json input body
response = requests.post(url, request_json)
assert response.status_code == 201

#fetch header from response
print(response.headers.get('Content-Type'))


#parse response to Json Format
response_json = json.loads(response.text)

#pick job key from object using Json path
job = jsonpath.jsonpath(request_json, 'job')
print(job)

