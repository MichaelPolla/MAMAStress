from jira import JIRA
import re

PROJECT_KEY="AMQP"

options = {
    'server': 'https://jira.spring.io'}
jira = JIRA(options)

# Get project
project = jira.project(PROJECT_KEY)

# Get components and version
components = jira.project_components(project)
versions = jira.project_versions(project)

# Get issues
issues = jira.search_issues("project="+PROJECT_KEY,maxResults=50000)
bugs=[]
for issue in issues:
    if(issue.fields.issuetype.name == "Bug"):
        print issue.fields.created
        bugs.append(issue)
