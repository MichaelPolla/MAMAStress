from jira import JIRA
import re
import csv

PROJECT_KEY="AMQP"

options = {
    'server': 'https://jira.spring.io'}
jira = JIRA(options)

# Get project
project = jira.project(PROJECT_KEY)

# Get components and version
print "Get versions..."
components = jira.project_components(project)
versions = jira.project_versions(project)

with open('csv_data/jira_versions.csv', 'wb') as csvfile:
    fieldnames = ["name", "release_date", "released"]
    writer = csv.DictWriter(csvfile,
        fieldnames=fieldnames)
    writer.writeheader()

    for version in versions:
        if(hasattr(version, 'releaseDate')):
            writer.writerow({ \
                "name" : version.name, \
                "release_date" : version.releaseDate, \
                "released" : int(version.released)
            })

# Get issues
print "Get issues..."
issues = jira.search_issues("project="+PROJECT_KEY,maxResults=50000)

# Write in csv
with open('csv_data/jira_issues_bugs.csv', 'wb') as csvfile:
    fieldnames = ["date", "summary"]
    writer = csv.DictWriter(csvfile,
        fieldnames=fieldnames)
    writer.writeheader()

    for issue in issues:
        # write only bugs
        if(issue.fields.issuetype.name == "Bug"):
            writer.writerow({ \
                "date" : issue.fields.created.replace(".000+0000", "Z"), \
                "summary" : issue.fields.summary
            })
