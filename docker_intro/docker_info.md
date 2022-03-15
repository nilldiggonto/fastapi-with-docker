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
    $ docker container 

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