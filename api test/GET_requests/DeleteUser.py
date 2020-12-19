import requests

#api url
url = "https://reqres.in/api/users?page=2"

response = requests.delete(url)

#fetch response code

print(response.status_code)

assert response.status_code == 204