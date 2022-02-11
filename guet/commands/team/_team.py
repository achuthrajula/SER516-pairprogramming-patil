import requests
import json
import sys

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

#print(response.text)



url = "https://api.taiga.io/api/v1/projects"

params = {'member': User_id } 


headers = {
  'Authorization': 'Bearer '+Auth  
}

response_1 = requests.request("GET", url, headers=headers, params=params)


#print(response.text)

#payload_1 = json.dumps({
 # "name": sys.argv[3]
#})


proj_name = input("Enter project name:   ")#sys.argv[3]
ABC = response_1.json()
for r in range(len(ABC)):
    if(proj_name == ABC[r]['name']):
        members = ABC[r]['members']

#print(members)
print("\nName of the members:\n")

for m in members:
    url = "https://api.taiga.io/api/v1/users/"+str(m)
    #params = {'member': m } 
    headers = {
        'Authorization': 'Bearer '+Auth
        }
    response_2 = requests.request("GET", url, headers=headers)
    mem = response_2.json()
    mem_1 = mem['full_name']
    print(mem_1,"\n")
    