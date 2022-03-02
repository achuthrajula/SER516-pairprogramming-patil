from email import message
import os 
from _path import ROOT_DIR

message =   """
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

try: 
    print(ROOT_DIR)
    file_exists = os.path.exists(ROOT_DIR + "/invite.md")


    if(file_exists):
        os.remove(ROOT_DIR + "/invite.md")

    f = open(f"{ROOT_DIR}/invite.md", "w")
    f.write(message)
    # f.close()

    #open and read the file after the appending:
    f = open(f"{ROOT_DIR}/invite.md", "w")
    print(f.read())

except Exception as e:
    print(e)