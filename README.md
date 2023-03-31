# Docker-kube Project

## Create an image 
- Create Docker Image from Dockerfile by following command  `docker build . -t my-app`

## Creating an container

- Run a Docker Image with following command `docker run -d --name my-app-ctr -p 8000:8000 my-app:latest`
 
 1. `-d` : deamon that run on background
 2. `--name`: give container name
 3. `-p` : for port mapping 
 
 and in laste give the image name and tage latest "my-app:latest"
