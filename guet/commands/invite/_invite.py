import os 
from _path import ROOT_DIR
from typing import List
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        self.sender_email = "jd8302543@gmail.com"
        self.sender_password = "jsdufkughae8324"
        self.receiver_email = ""
        self.email_message = """\
<html>
  <body>
    <p>Hey there,<br>
        This is an invitation to collaborate<br><br>
        What is guet?<br>
        It is a tool to help you track the collaborative contributions of your team.<br><br>
        Why should I join?<br>
        We're a small team of developers who want to make the world a better place. We are looking for people who are passionate about open source and want to contribute to the open source community. <br><br>
        We hope you will join us and contribute by being a part of our pair programming session.<br><br>
        ~ Team Pair Programming Patil
    </p>
  </body>
</html>
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
            print("Invite.md sucessfully created")

        except Exception as e:
            # Handle exception and notify user
            print(f"Invite command failed due to: {e}")

        try:
            print(len(args))
            # A scenario where the user has not provided his/her credentials
            if len(args) == 1:
                self.receiver_email = args[0]

            # A scenario where the user has not provided his/her credentials but gave custom message
            elif len(args) == 2:
                self.receiver_email = args[0]
                self.message = args[1]

            # A scenario where the user has provided his/her credentials but didn't provide custom message
            elif len(args) == 3:
                self.sender_email = args[0]
                self.sender_password = args[1]
                self.receiver_email = args[2]

            # A where the user has provided his/her credentials and custom message 
            elif len(args) == 4:
                self.sender_email = args[0]
                self.sender_password = args[1]
                self.receiver_email = args[2]
                self.email_message = args[3]
            
            else:
                pass

        except Exception as e:
            # Handle exception and notify user
            print(f"Email service command failed due to: {e}")

        else: 
            # Fill email body
            message = MIMEMultipart("alternative")
            message["Subject"] = "Open invitation to collaborate"
            message["From"] = self.sender_email
            message["To"] = self.receiver_email

            # Specify MIMEText objects as HTML
            content = MIMEText(self.email_message, "html")

            message.attach(content)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(
                    self.sender_email, self.receiver_email, message.as_string()
                )
            print("Invitation sent successfully")