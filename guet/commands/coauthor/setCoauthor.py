import requests
import json
from guet.steps.action import Action
from typing import List


class SetCoauthor(Action):
    def __init__(self):
        super().__init__()

    def execute(self, args: List[str]):

        print('Trying to add co-author to the task via comment')
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

        user = response.json()
        auth_token = user['auth_token']
        url = "https://api.taiga.io/api/v1/tasks?project=438216"
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        task_name = args[2]
        response_payload = response.json()

        for r in range(len(response_payload)):
            if(task_name == response_payload[r]['subject']):

                id = response_payload[r]['id']
                version = response_payload[r]['version']
                comm = args[3]
                url = f"https://api.taiga.io/api/v1/tasks/{id}"
                payload = {
                    "version": f"{version}",
                    "comment": f"@{comm}"
                }
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth_token}"
                }

                response = requests.request(
                    "PATCH", url, json=payload, headers=headers)

                print("Successfully added co-author")
