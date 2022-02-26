import requests
import json
import sys
from guet.steps.action import Action

class SetCoauthor(Action):
    def __init__(self):
        super().__init__()



url = "https://api.taiga.io/api/v1/auth?"

payload = json.dumps({
  "username": sys.argv[1],
  "password": sys.argv[2],
  "type": "normal"
  
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

user = response.json()
User_id = user['id']
Auth = user['auth_token']


url = "https://api.taiga.io/api/v1/tasks?project=438216"

payload = ""
headers = {}

response_1 = requests.request("GET", url, headers=headers, data=payload)

#print(response_1.text)

task_name = input("Enter task subject:   ")#sys.argv[3]
ABC = response_1.json()
for r in range(len(ABC)):
    if(task_name == ABC[r]['subject']):
        id = ABC[r]['id']
        version = ABC[r]['version']
        #print(version)
        comm = input("Please enter your message for co-author : ")
        url = "https://api.taiga.io/api/v1/tasks/"+str(id)
        payload = "{\n\t\"version\":"+str(version)+",\n\t\"comment\": \""+'@'+comm+"\"\n}"
        headers = {
            'content-type': "application/json",
            'authorization': 'Bearer '+Auth,
            'cache-control': "no-cache",
            'postman-token': "3efa9b41-3192-b4ba-ff77-679f0d9c8cd2"
            }

response_2 = requests.request("PATCH", url, data=payload, headers=headers)
