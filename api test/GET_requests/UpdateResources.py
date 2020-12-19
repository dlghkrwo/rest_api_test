import requests
import json
import jsonpath

#sending update data in the requests json and getting response
#this time its not creating new resource on the server it is updating on existing server 

# api url
url = "https://reqres.in/api/users?page=2"

#read input json file
file = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\creatingUser.json', 'r') # read the file
json_input = file.read() #reading the file from the content and store in the variable
request_json = json.loads(json_input) #loads will do parse the data into json format


#make PUT request with Json input body
response = requests.put(url, request_json)
assert response.status_code == 200

#parse response content
#whatever the data we are getting in the response im parsing the response into form of json and i can fetch any value
response_json = json.loads(response.text)
update_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(update_li[0])
