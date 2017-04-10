# MAMAStress
The best JIRA/GitHub software to get the stress of the team when the deadline approches

## Authors
- **M**ichael Polla
- **A**na Domingos
- **M**axime Burri
- **A**ntoine Berger
- **S**alvatore Cicciu

## Installation
`pip install jira`

## Tokens
Github : under 60 requests, no token is required. To be able to make more requests, generate a token :
1. Go to https://github.com/settings/tokens
2. Generate token
3. Copy token and pass it as argument  
  
JIRA : no token required.

## Build and Run all services
In directory Dockers, make these commands in this order:

`$ export TOKEN=yourgithubtoken`

`$ docker-compose up`


## Examples
`python jira_retriever.py`
`python github_retriever.py [access_token]`
