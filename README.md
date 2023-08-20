# Doc-Kube-Project

#Image

Creat an Image
    

    docker build . -t my-app


Creating an Container


    docker run -d --name my-app-ctr -p 8000:800 my-app:latest


Details

    -d : deamon that run on background
    --name: give container name
    -p : for port mapping 
    my-app:latest:  in last give the image name and tage latest 


Docker Compose: 
Docker compose is a tool defining and running multi-container Docker applications. It allows you to define your application's. It allows you to define your application services, networks and volumes in single "docker-compose.yml" it spin all the containers in single command.  This is useful for running complex applications that require multiple services, such as web applications that rely on databases and caching services.

    docker-compose up
    docker-compose down
website




    pip install -r requirements.txt
    

