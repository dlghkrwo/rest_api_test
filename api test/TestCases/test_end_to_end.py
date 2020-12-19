import requests
import json
import jsonpath

#ready to post the request file, reading the content of the file. whatever i read from the open file, i will read
# as json file and fetching the complete data.
#end to end testing adding student, updating technicalskills, updating address and then we are getting response
#

#adding a new student and we fetch its id then add technical details, 
def test_add_new_data():
    App_url = "http://http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\creatingUser.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_url, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    #post request with url
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\TechDetails.json', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/address"
    f = open('C:\\Users\\dlghk\\OneDrive\\바탕 화면\\python\\api test\\address.json', 'r')
    request_json = json.loads(f.read())
    request_json['stid'] = id[0]
    print(response.text)

    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" +str(id[0])
    response = requests.get(final_details)
    print(response.text)