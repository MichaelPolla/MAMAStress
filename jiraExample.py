from jira import JIRA
import re

PROJECT_KEY="AMQP"

options = {
    'server': 'https://jira.spring.io'}
jira = JIRA(options)

# Get project
project = jira.project(PROJECT_KEY)
print project.id

# Get components and version
components = jira.project_components(project)
versions = jira.project_versions(project)
print components
print versions
