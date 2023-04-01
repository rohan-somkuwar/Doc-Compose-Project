# Doc-Kube-Project

create an image 

"docker build . -t my-app"

creating an container

"docker run -d --name my-app-ctr -p 8000:800 my-app:latest"
  -d : deamon that run on background
  --name: give container name
  -p : for port mapping 
  and in laste give the image name and tage latest "my-app:latest"
