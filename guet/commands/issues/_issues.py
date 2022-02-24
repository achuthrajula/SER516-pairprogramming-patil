from github import Github
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Issues Name", "Issue ID"]

# Get access token and repo path from user
access_token, path_to_repo = input("Enter your access token and path to your repository: ").split(" ")

# Login with access token
g = Github(access_token)

# Get the user
user  = g.get_user()

# Get all repositories
my_repos = user.get_repos()

# Fetch all open issues in the specified repository
repo = g.get_repo(path_to_repo)
open_issues = repo.get_issues(state='open')

# Print the issues in a pretty table

for issue  in open_issues:
    issue_name = issue.title
    issue_id = issue.number
    table.add_row([issue_name, issue_id])

print(table)