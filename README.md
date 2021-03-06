# guet

> enable contribution tracking when pair programming with guet

Pair programming is integral part of many software development lifecycles. When pairing, you may want to track each committer's contributions. Using **guet** enables that functionality without changing the normal git workflow.

[![Actions Status](https://github.com/chiptopher/guet/workflows/guetci/badge.svg)](https://github.com/chiptopher/guet/workflows/guetci/badge.svg)
[![PyPI version](https://badge.fury.io/py/guet.svg)](https://badge.fury.io/py/guet)
![PyPI - Downloads](https://img.shields.io/pypi/dm/guet)

## Installation

**guet** should be installed locally:

After cloning this repository run the following commands from the root directory of the repository
```
sudo python3 setup.py develop
```
```
pip3 install -r requirements.txt
```

## Usage

### Launching the GUI
```
guet
```

### init

Initialize repository for guet tracking.

```
$ init
```

| Flag                        | Description                          |
| --------------------------- | ------------------------------------ |
| --location [path to foler]  | Specify directory to create hooks in |
| --alongside / -a            | Append -guet to hook file names      |
| --overwrite / -o            | Overwrite existing hooks             |


### add

Add a committer for commit tracking
OR
Add multiple committers for commit tracking at once

```
$ add p1 "Person 1" person@example.com

$ add p1 "Person 1" person1@example.com p2 "Person 2" person2@example.com 

```

| Flag                        | Description                           |
| --------------------------- | ------------------------------------  |
| --local                     | Add users locally to this repository (and create local configuration files |


### set

Set committers for current repository

```
$ set p1 p2
Committers set to:
p1 - Person 1 <person1@example.com>
p2 - Person 2 <person2@example.com>
```

### get

Get committers.

```
$ get all
All committers
p1 - Person 1 <person1@example.com>
p2 - Person 2 <person2@example.com>
p3 - Person 2 <person2@example.com>

$ get current
Current committers
p1 - Person 1 <person1@example.com>
p3 - Person 2 <person2@example.com>

$ get pair-log
Displays the data of tracked pair programming sessions
```

### remove

Remove committer
OR
Remove multiple committers at once

```
$ remove p1

$ remove p1 p2 p3

```

### taiga-teammates

Get Taiga teammates

```
$ taiga-teammates <taiga_username> <taiga_password> <project_name>
```

### issues
Fetch open issues from GitHub Repository

```
$ issues <GitHub_access_token> <repository_path>
```

### pair
Indicate Pairing Strategy

```
$ pair roles <username> <password> <sprint_option> <userstory_option>
Get roles of teammates from taiga project

$ pair <pairing_strategy> <initials_of_committer1> <initials_of_committer2>
Set the pairing strategy by providing the pairing strategy and initials of both the committers

$ pair clear-log
Clears the log file containing the tracking data of pair programming sessions
```

### co-author
Sets co-author in a comment for a task

```
$ co-author <username> <password> <Task-subject> <message for the co-author of the task>

```

### invite

Send invitation to collaborate via GitHub repo and email

```
$ invite 
Send invitation by adding invitation to the repo

$ invite <receiver_email>
Send invitation by adding invitation to the repo and email to the specified email with default email client and message

$ invite <receiver_email> <message>
Send invitation by adding invitation to the repo and email to the specified email and message with default email client

$ invite <receiver_email> <message>
Send invitation by adding invitation to the repo and email to the specified email and message with default email client

$ invite <sender_email> <sender_password> <receiver_email> 
Send invitation by adding invitation to the repo and email using specified email and password with default message

$ invite <sender_email> <sender_password> <receiver_email> <message>
Send invitation by adding invitation to the repo and email using specified email and password with custom message
```

### yeet

Remove guet configurations.

```
$ yeet
```

| Flag                        | Description                           |
| --------------------------- | ------------------------------------  |
| --global / -g               | Remove guet configuration from home directory
