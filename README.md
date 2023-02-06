# YOTAM HALPERIN PORTFOLIO

### Crossy Road is a python flask app that can run either localy or in the cloud.
### you can download the CrossyRoad game in the website, to register for updates,
### And you can view the leaderboard of all the other players that has played in 
### this game before...  


##### to run localy:

docker compose build
docker compose up

- you can now visit 'localhost:80' on your browser to view the flask application.
- to download the game- navigate to the 'download' section and press the download button

##### to start CI with Jenkins multibranch pipeline:

##### change the enviroment variables in the jenkinsfile
- GITHUB_CREDS      -> name of the jenkins credentials ID to authenticate with github
- DOCKERHUB_REPO    -> name of the DockerHub repo that the artifact is pushed to
- DOCKERHUB_CREDS   -> name of the jenkins credentials ID to authenticate with dockerhub 

##### to add Jenkins Gloabal Credentials
- Go to Manage Jenkins > Manage Credentials > System > Global credentials (unrestricted) > Add Credentials

