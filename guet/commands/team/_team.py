import json
import requests
from typing import List

from guet.steps.action import Action


class GetTaigaTeammates(Action):

    def __init__(self):
        super().__init__()

    def execute(self, args: List[str]):

        # Making a request to Taiga API
        # by passing command line arguments
        # to obtain auth token form Taiga server

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
        user_id = user['id']
        auth = user['auth_token']
        url = "https://api.taiga.io/api/v1/projects"

        print('Authorization: Done\n')

        # Using the obtained auth token
        # to get the details of the project

        params = {'member': user_id}

        headers = {
            'Authorization': 'Bearer ' + auth
        }

        response = requests.request(
            "GET", url, headers=headers, params=params)

        project_name = args[2]
        project_response = response.json()

        print('Fetching project data: Done\n')

        for r in range(len(project_response)):
            if(project_name == project_response[r]['name']):
                user_ids = project_response[r]['members']

        # From the fetched project details
        # retrieving the details of the teammates

        teammates = []
        for user_id in user_ids:
            url = "https://api.taiga.io/api/v1/users/"+str(user_id)
            headers = {
                'Authorization': 'Bearer ' + auth
            }
            response = requests.request("GET", url, headers=headers)
            user = response.json()
            name = user['full_name']
            teammates.append(name)

        print('Fetching teammates from project: Done\n')

        print("Teammates: ", teammates)
