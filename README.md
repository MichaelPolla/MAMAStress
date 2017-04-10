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
For github does not need a token there, but if the limit is reached (60 requests), we can generate a code to have more requests :
1. go to https://github.com/settings/tokens
2. generate token
3. copy token and pass as arguments

For JIRA does not need a token.

## Build and Run all services
In directory Dockers, make this command:

`$ docker-compose up`


## Examples
`python jira_retriever.py`
`python github_retriever.py [access_token]`
