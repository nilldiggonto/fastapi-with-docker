## DOCKER

*   Docker version
    ```
    docker version
    ```
*   Docker Image (A kind of VM)
    * To check image list
    ```
    $ docker image ls
    $ docker images
    ```
    * Pulling a kali-linux image
    ```
    // docker image pull <repository>:<tag> 
    // hub.docker.com
    $ docker image pull kalilinux/kali-rolling
    $ docker image pull ubuntu:latest

    // for multiple image
    $ docker image pull ubuntu:latest and docker image pull mongo:latest

    // for multiple tags
    $ docker image pull -a <repository>

    // Filter Images
    $ docker images <image-name>
    $ docker images <image-name*> //related

    // Format Images
    $ docker images --format "{{.Repository}}:{{.Tag}}:{{.Size}}"

    // Inspect Image
    $ docker image inspect <respository-name>

    // Digest Image
    $ docker images --digests ubuntu:latest

    // Only Return image ID
    $ docker images -q

    // remove images
    $ docker image rm <repository-name>
    $ docker image rm -f <repository-name>
    // Delete All Image
    $ docker image rm $(docker image ls -q) -f
    ```
    
*   Docker Search from CLI (hub.docker.com)
    * https://docs.docker.com/engine/reference/commandline/search/
    ```
    $ docker search nginx
    $ docker search --filter stars=3 nginx
    ```
*   Docker Containers
    * Run a container
    ```
    $ docker container run -it kalilinux/kali-rolling /bin/bash

    // contianer list
    $ docker container ls

    // attach to a container
    $ docker container exec -it <contianer-name/ID> bash

    // Stop a container
    $ docker container stop <ID/container-name>

    // To remove a container
    $ docker container -r <ID/COntainer-name>

    // To see all running and stop container activity
    $ docker container ls -a
    ```

#### FASTAPI WITH DOCKER
* For Postgres
    ```
    $ docker image pull postgres:alpine
    ```
* Creating the Container
    ```
    $ docker run --name <whatever-name> -e POSTGRES_PASSWORD=123456 -d -p 5432:5432 postgres:alpine
    ```
* Check Container
    ```
    $ docker ps
    ```
* CLI MODE

    ```
    $ docker exec -it <whatever-name> bash

    // DB SETUP
    $ psql -U postgres

    $ CREATE DATABASE <whatever-name>;
    $ CREATE USER <username> WITH ENCRYPTED PASSWORD '123456';
    $ GRANT ALL PRIVILEGES on DATABASE <whatever-name> to <username>;

    // connect to DB and ACCESS FOR outside container
    $ \c <whatever-db>
    $ psql -h localhost -p 5432 postgres
    ```
    
