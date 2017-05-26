# MAMAStress
JIRA/GitHub scripts with dockers to get the stress of the team when the deadline approches

## Authors
- **M**ichael Polla
- **A**na Domingos
- **M**axime Burri
- **A**ntoine Berger
- **S**alvatore Cicciu

## Build and Run all services

### Token Github
Github : under 60 requests, no token is required. To be able to make more requests, generate a token :
1. Go to https://github.com/settings/tokens
2. Generate token
3. Copy token and pass it as argument  
  
```bash
export TOKEN=yourgithubtoken
```

### Set tup the project to analysis
There are three variables for set up the project : `GITHUB_REPO`, `JIRA_PROJECT`, `JIRA_SERVER`

Exemple :
- AMQP :
```bash
export GITHUB_REPO="spring-projects/spring-amqp"
export JIRA_PROJECT="AMQP"
export JIRA_SERVER="https://jira.spring.io"
```
- DATAREDIS :
```bash
export GITHUB_REPO="spring-projects/spring-data-redis"
export JIRA_PROJECT="DATAREDIS"
export JIRA_SERVER="https://jira.spring.io"
```
- Spring framework :
```bash
export GITHUB_REPO="spring-projects/spring-framework"
export JIRA_PROJECT="SPR"
export JIRA_SERVER="https://jira.spring.io"
```

### Run
After configuration, just run this command : ```bash
docker-compose up```

