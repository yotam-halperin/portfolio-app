# YOTAM HALPERIN PORTFOLIO

### Crossy Road is a python flask app that can run either localy or in the cloud.
### you can download the CrossyRoad game in the website, to register for updates,
### And you can view the leaderboard of all the other players that has played in 
### this game before...  

##### to create executable of the crossyroad application type the following command in the crossyroad folder 
pyinstaller crossy_main.py -w --onefile

- pull crossy_road executable from 'dist' folder to 'crossy_road' folder
- delete 'dist' 'build' folders and 'crossy_main.spec' file
- zip 'crossy_main' folder with "zip -r crossy_main.zip crossy_main/"  
- put the ziped file in 'flask' directory


##### to run localy:

clean the enviroment:
- docker compose down -v

build the images:
- docker compose build

start the application:
- docker compose up

- you can now visit 'localhost:80' on your browser to view the flask application.
- to download the game- navigate to the 'download' section and press the download button

##### to start CI with Jenkins multibranch pipeline:

##### change the enviroment variables in the jenkinsfile
- GITHUB_CREDS              -> name of the jenkins credentials ID to authenticate with github
- DOCKERHUB_BACKEND_REPO    -> name of the DockerHub repo that the backend (application) artifact is pushed to
- DOCKERHUB_FRONTEND_REPO   -> name of the DockerHub repo that the frontend (static files) artifact is pushed to
- DOCKERHUB_CREDS           -> name of the jenkins credentials ID to authenticate with dockerhub 
- YH_MYSQL_PASSWORD         -> name of the data base password - *in plain text, only for CI porpuses
- YH_MYSQL_HOST             -> name of the mysql service


##### to add Jenkins Gloabal Credentials
- Go to Manage Jenkins > Manage Credentials > System > Global credentials (unrestricted) > Add Credentials

- To set the jenkins server
- the jenkins Dockerfile looks like this:

<!-- 
FROM jenkins/jenkins:lts-jdk11
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

USER jenkins 
-->

docker build -t jenkinsserver .

docker run -p 8080:8080 --name jenkins -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -dit jenkinsserver bash

- visit localhost:8080


