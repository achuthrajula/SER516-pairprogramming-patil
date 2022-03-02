import os 
from _path import ROOT_DIR
from typing import List

from guet.steps.action import Action

class SendInvite(Action):
    def __init__(self):
        super().__init__()
        self.message = """
## An open invitation to collaborate
<br />

####  What is guet?
#### It is a tool to help you track the collaborative contributions of your team.
<br />

#### Why should I join?
#### We're a small team of developers who want to make the world a better place.
#### We are looking for people who are passionate about open source and want to contribute to the open source community.
<br />

#### We hope you will join us and contribute by being a part of our pair programming session.

<pre>
                                            ~   Team Pair Programming Patil
</pre>
"""

    def execute(self, args: List[str]):

        try: 
            # Check if the file exists
            file_exists = os.path.exists(ROOT_DIR + "/invite.md")

            # If the file exists, remove it from the directory
            if(file_exists):
                os.remove(ROOT_DIR + "/invite.md")

            # Create a new file and add the invitation message
            f = open(f"{ROOT_DIR}/invite.md", "w")
            f.write(self.message)
            f.close()

            # Send acknowledgement to the user
            f = open(f"{ROOT_DIR}/invite.md", "w")
            print(f.read())

        except Exception as e:
            # Handle exception and notify user
            print(f"Invite command failed due to: {e}")