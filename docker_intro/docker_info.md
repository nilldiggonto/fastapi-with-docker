* Docker
    ```
    $ docker --version
    $ docker info
    $ docker
    ```
    * Nginx Image
    ```
    $ docker container run --publish 80:80 nginx 
    $ docker container run --publish 80:80 --detach nginx (run in background)
    $ docker container run --publish 80:80 --detach --name webhost nginx
    $ docker container logs webhost
    $ docker container top webhost
    
    ```
    * Container
    ```
    $ docker container ls
    $ docker cotainer stop CONTAINER_ID
    $ docker container ls -a (List of all container)
    $ docker container rm CONTAINER_ID(Remove container)
    $ docker container rm -f CONTAINER_ID(Force Remove)
    $ docker container inspect CONTAINER_ID
    $ docker container stats


    ```

    * Mongo
    ```
    $ docker run --name mongo -d mongo (Create mongo image and run in background)
    $ docker top mongo 
    $ docker stop mongo
    ```

    * Mysql
    ```
    $ docker container run -d -p 3306:3306 --name mdb -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql (w8UTtS2ljzG29C4ri2mkgsQoNZbFMKWl)
    $ docker container logs mdb
    ```
    * Apache
    ```
    $ docker container run -d --name webserver -p 8080:80 httpd
    ```

    * Interactive Container
    ```
    $ docker container run -it --name proxy nginx bash
    $ docker container run -it --name ubuntu ubuntu
    $ docker container start -ai ubuntu (reRUn container)

    $ docker container exec -it mysql bash (existing container bash)
    ```

    * Docker Image
    ```
    $ docker pull IMAGE_NAME
    $ docker image ls
    ```

    * Docker Network
    ```
    $ docker container port CONTAINERID
    $ docker container inspect --format '{{ .NetworkSettings.IPAddress}}' CONTAINERID
    $ docker container port webhost (Know the port service running)

    $ docker network ls (show all network)
    $ docker network create dummy_net (create a network)
    $ docker container run -d --name new_nginx --network dummy_net nginx

    //connect to network
    $ docker network connect network_id container_id
    //disconnect to network
    $ docker network disconnect networkd_id container_id
    ```

    * DNS
    ```
    $ docker container exec -it container_nginx ping another_container_nginx (same network)

    //Auto cleaning
    $ docker container run --rm -it centos:7 bash
    $ docker container run --rm -it ubuntu:14.04 bash

    // DNS ROUND ROBIN
    $ docker network create 
    $ docker container run -d --net robin --net-alias search elasticsearch:2 (creating network alias)

    $ docker container run --rm --net robin alpine nslookup search
    $ docker container run --rm --net robin centos curl -s search:9200

    ```
    * images
    ```
    $ docker image ls
    $ dokcer pull nginx (pull from hub.docker.com)
    $ docker history IMAGENAME
    $ docker inspect IMAGENAME
    
    ```
    * Building image
    ```
    $ docker image build -t customnginx .  
    $ docker container run --rm -p 80:80 customnginx
    $ docker image tag customnginx:latest nilldiggonto/customnginx:latest 
    $ docker push nilldiggonto/customnginx:latest
    $ docker image rm nilldiggonto/customnginx:latest
    $ docker image prune (Remove unused images)
    $ docker system prune (Clean everything)
    ```
    * Docker Volume
    ```
    $ docker volume prune (remove unused volume)
    $ docker pull mysql
    $ docker inspect mysql
    $ docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
    $ docker volume ls (list of volume)
    
    //bind mounting
    $ cat Dockerfile
    $ docker container run -d --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx
    //
    

    // naming volume
    $ docker container run -d --name psql -v psql:/var/lib/postgresql/data postgres:9.6.1
    $ docker container logs -f psql
    ```

