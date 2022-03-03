from typing import List
from plyer import notification
import requests
import logging
import json
import sys
import datetime
import time

from guet.committers import Committers2 as Committers
from guet.committers import CurrentCommitters
from guet.steps.action import Action


class PairCommittersAction(Action):
    def __init__(self,
                 committers: Committers,
                 current_committers: CurrentCommitters):
        super().__init__()
        self.committers = committers
        self.current_committers = current_committers

    def execute(self, args: List[str]):
        if args[0].lower() == "roles":
            data = {"password": str(args[2]), "username": str(args[1]), "type": "normal"}
            resp = requests.post('https://api.taiga.io/api/v1/auth', json=data)


            token = ""
            if resp.status_code != 200:
                print("Error")
            else:
                token = format(resp.json()["auth_token"])

            data = {"AUTH_TOKEN": token}

            resp = requests.get(
                "https://api.taiga.io/api/v1/projects/by_slug?slug=agiliyal-pairprogramming-patil-team-ser-516-project-1", json=data
            )

            for values in resp.json():
                if values == "task_statuses":
                    for task_statuses in resp.json()["task_statuses"]:
                        project_id = str(task_statuses["project_id"])


            resp = requests.get('https://api.taiga.io/api/v1/milestones?project='+project_id, json=data)
            sprint_id = 0
            sprint_name = []
            milestones_id = []
            user_stories= {}
            sprints = []
            for values in resp.json():
                sprint_id = sprint_id + 1
                sprint_name.append(values["name"])
                user_stories = values["user_stories"]
                milestones_id.append(values["id"])
            sprint_option = int(args[3])
            print(f"Selected sprint is {sprint_name[sprint_option]}\n")
            current_sprint = milestones_id[sprint_option]
            current_sprint_us =[]
            for values in resp.json():
                user_story_id = 0
                
                for us in values["user_stories"]:
                    if us["milestone"] == current_sprint:
                        current_sprint_us.append(str(us["subject"]))
                        user_story_id = user_story_id + 1
            user_story_option = int(args[4])
            print(f'selected user story is {current_sprint_us[user_story_option]}n')
            resp = requests.get(
                "https://api.taiga.io/api/v1/projects/by_slug?slug=agiliyal-pairprogramming-patil-team-ser-516-project-1", json=data
            )
            member_id = []
            member_names = []
            for values in resp.json():
                if values == "members":
                    print("The team members are - ")
                    for members in resp.json()["members"]:
                        member_id.append(members["id"])
                        member_names.append(members["full_name"])
                        print(members["full_name_display"] + ": " + members["role_name"]+"\n")
        elif args[0] =="clear-log":
            file = open("logfile.log","r+")
            file.truncate(0)
            file.close()
  
        else:
            strategies = {
                "do" : ["Driver","Observer"],
                "sj" : ["Senior", "Junior"]
            }
            pairing_strategy = args[0].lower()
            if pairing_strategy in ["do","sj"]:
                committer_initials = [arg.lower() for arg in args[1:3]]
                found = [committer for committer in self.committers.all() if committer.initials in committer_initials]
                if pairing_strategy == "do":
                    final_strategy = strategies['do']
                else:
                    final_strategy = strategies['sj']
                for i in range(2):
                    for j in ["Driver","Observer","Senior","Junior"]:
                            if j in found[i].name:
                                found[i].name = found[i].name.replace(f"({j})","")

                if committer_initials[0] == found[0].initials:
                        print(found[0].name)
                        found[0].name = f"{found[0].name}({final_strategy[0]})"
                        print(found[0].name)
                        found[1].name = f"{found[1].name}({final_strategy[1]})"
                else:
                        found[0].name = f"{found[0].name}({final_strategy[1]})"
                        found[1].name = f"{found[1].name}({final_strategy[0]})"
                for i in range(0,2):
                    self.committers.remove(found[i].initials)
                    self.committers.add(found[i])
                    
                self.current_committers.set(found)    
                print(f"Current pairing strategy is {final_strategy[0]} and {final_strategy[1]}\n {found[0].name} \n {found[1].name}")
            else:
                print("Enter a valid pairing strategy")