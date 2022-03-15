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
    $ 
    ```