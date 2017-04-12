import requests
import json
import sys
import csv
import os

GITHUB_OWNER_REPO = "spring-projects/spring-amqp"

access_token = None

PATH = 'csv_data/'

if(len(sys.argv) > 1):
    access_token = sys.argv[1]

if(len(sys.argv) > 2):
    GITHUB_OWNER_REPO = sys.argv[2]

if(len(sys.argv) > 3):
	PATH=sys.argv[3]

if not os.path.exists(PATH):
	os.makedirs(PATH)

GITHUB_OWNER_REPO_API = "https://api.github.com/repos/"+GITHUB_OWNER_REPO

#Request : https://api.github.com/repos/spring-projects/spring-amqp/commits
#Doc : https://developer.github.com/v3/repos/commits/
def commits():
    allCommits = []
    i = 1
    while True:
        # Params and access token
        params = "page="+str(i)+"&per_page=100"
        if(access_token != None):
            params += "&access_token="+access_token

        # Request and load
        r = requests.get(GITHUB_OWNER_REPO_API+"/commits", params)
        commits = json.loads(r.content)
        print "remaining-rate:"+str(r.headers['X-RateLimit-Remaining']) + \
            " reset:"+str(r.headers['X-RateLimit-Reset']) + \
            " page:"+str(i) + \
            " len:"+str(len(commits))

        # Check rate limit
        if(int(r.headers['X-RateLimit-Remaining']) == 0):
            print "No more rate.... generate other access_token..."
            exit()

        # While not end, continue
        if(len(commits)==0):
            break
        else:
            allCommits+=commits
            i+=1
    return allCommits

commits = commits()
# Get date of last commit
print str(len(commits))
print json.dumps(commits[0])
with open(PATH+'github_commits.csv', 'wb') as csvfile:
    fieldnames = ["date", "name_first_line"]
    writer = csv.DictWriter(csvfile,
        fieldnames=fieldnames)
    writer.writeheader()

    for commit in commits:
        writer.writerow({ \
            "date" : commit['commit']['committer']['date'], \
            "name_first_line" : commit['commit']['message'].split('\n', 1)[0]
        })


# Open a file
fo = open(PATH+"github_retriever.txt", "wb")

# Close opend file
fo.close()
