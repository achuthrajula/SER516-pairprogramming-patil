import requests
import json
import sys
import datetime
import time

# Login authentication --- Enter your Password and Username for Taiga to get all the information
data = {"password": "Giliyal1997?", "username": "agiliyal@asu.edu", "type": "normal"}
resp = requests.post("https://api.taiga.io/api/v1/auth", json=data)


token = ""
if resp.status_code != 200:
    print("Error")
else:
    token = format(resp.json()["auth_token"])

data = {"AUTH_TOKEN": token}

resp = requests.get(
    "https://api.taiga.io/api/v1/projects/by_slug?slug=agiliyal-pairprogramming-patil-team-ser-516-project-1",
    json=data,
)

for values in resp.json():
    if values == "task_statuses":
        for task_statuses in resp.json()["task_statuses"]:
            project_id = str(task_statuses["project_id"])


# print("The Sprints in this Project are:\n")
resp = requests.get(
    "https://api.taiga.io/api/v1/milestones?project=" + project_id, json=data
)
sprint_id = 0
sprint_name = []
milestones_id = []
user_stories = {}
sprint_list = []
for values in resp.json():
    sprint_id = sprint_id + 1
    sprint_name.append(values["name"])
    milestones_id.append(values["id"])

vk = 0
ag = 0
ar = 0
sp = 0

for sprint_id in milestones_id:
    task_resp = requests.get(
        "https://api.taiga.io/api/v1/tasks?project="
        + str(project_id)
        + "&milestone="
        + str(sprint_id),
        json=data,
    )
    for values in task_resp.json():
        if values["assigned_to_extra_info"] is None:
            full_name_display = "None"
        else:
            for assigned_to_extra_info in values["assigned_to_extra_info"]:
                assignedTo = values["assigned_to_extra_info"]
                full_name_display = assignedTo["full_name_display"]

            if full_name_display == "Varshik Sonti":
                vk += 1
            elif full_name_display == "Achuth Reddy Rajula ":
                ar += 1
            elif full_name_display == "Shivani Sanjay Patil":
                sp += 1
            elif full_name_display == "Apoorva Giliyal":
                ag += 1

best_pair = {
    "Varshik Sonti": vk,
    "Achuth Rajula": ar,
    "Shivani Patil": sp,
    "Apoorva Giliyal": ag,
}
my_keys = sorted(best_pair, key=best_pair.get, reverse=True)[:2]
print(my_keys)
