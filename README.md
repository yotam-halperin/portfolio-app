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

- To set the jenkins server: OPTION 1 ( using docker compose && Dockerfile )

<!-- version: '3'

services:
  jenkins:
    build: ./jenkins/
    ports:
      - "8080:8080"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock -->

- the jenkins dockerfile looks like this:

<!-- FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean:1.26.0 docker-workflow:563.vd5d2e5c4007f"
USER root
RUN groupadd docker && usermod -aG docker jenkins && newgrp docker
RUN apt-get update
RUN apt-get install docker-compose-plugin

USER jenkins -->



- To set the jenkins server: OPTION 2 ( using imperative commands )

docker run -p 8080:8080 --name jenkins -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -dit jenkins/jenkins:lts-jdk11 bash

install docker on the server
install docker-compose on the server


