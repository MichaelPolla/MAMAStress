import requests
import json

GITHUB_OWNER_REPO = "spring-projects/spring-amqp"
GITHUB_OWNER_REPO_API = "https://api.github.com/repos/"+GITHUB_OWNER_REPO

#Request : https://api.github.com/repos/spring-projects/spring-amqp/commits
#Doc : https://developer.github.com/v3/repos/commits/
def commits():
    r = requests.get(GITHUB_OWNER_REPO_API+"/commits")
    return json.loads(r.content)

commits = commits()
# Get date of last commit
print commits[0]['commit']['committer']['date']
