import requests
import json
import sys
from guet.steps.action import Action
from typing import List

class SetCoauthor(Action):
    def __init__(self):
        super().__init__()

    def execute(self, args: List[str]):

      print(args)

      url = "https://api.taiga.io/api/v1/auth?"

      payload = json.dumps({
        "username": args[0],
        "password": args[1],
        "type": "normal"
        
      })
      headers = {
        'Content-Type': 'application/json'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      # print(response.text)
      user = response.json()
      User_id = user['id']
      Auth = user['auth_token']


      url = "https://api.taiga.io/api/v1/tasks?project=438216"

      payload = ""
      headers = {}

      response_1 = requests.request("GET", url, headers=headers, data=payload)

      # print(response_1.text)

      task_name = args[2]
      ABC = response_1.json()
      for r in range(len(ABC)):
        if(task_name == ABC[r]['subject']):
          id = ABC[r]['id']
          version = ABC[r]['version']

          # print(id, version)
          #print(version)
          comm = args[3]
          # print(comm)

          url = f"https://api.taiga.io/api/v1/tasks/{id}"

          # print(url)

          payload = {
              "version": f"{version}",
              "comment": f"@{comm}"
          }
          headers = {
              "Content-Type": "application/json",
              "Authorization": f"Bearer {Auth}"
          }

          response = requests.request("PATCH", url, json=payload, headers=headers)

          print("Successfully added co-author")