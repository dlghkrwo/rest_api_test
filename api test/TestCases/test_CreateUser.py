import requests
import json
import jsonpath

#how i can convert testcase into pytest format then execute testcases using pytest
# and write multiple testcases in a file

# api url
url = "https://reqres.in/api/users"

def test_create_new_user():
    file = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\creatingUser.json', 'r') 
    json_input = file.read()
    request_json = json.loads(json_input) 
    response = requests.post(url, request_json)

    assert response.status_code == 201


def test_create_other_user():
    file = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\creatingUser.json', 'r') 
    json_input = file.read()
    request_json = json.loads(json_input) 
    response = requests.post(url, request_json)

    response_json = json.loads(response.text)
    job = jsonpath.jsonpath(request_json, 'job')
    print(job)
    

