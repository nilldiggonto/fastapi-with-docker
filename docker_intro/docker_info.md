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

    * docker-compose
    ```
    $ docker-compose up
    $ docker-compose down -v
    $ docker-compose down --rmi local (Delete local images)
    ```

    * Swarm
    ```
    $ docker swarm init
    $ docker swarm init --advertise-addr 192.168.0.1:2377

    $ docker node ls (manager)
    ```
    * Service
    ```
    $ docker service create alpine ping 8.8.8.8
    $ docker service ls
    $ docker service ps SERVICE_NAME

    //scale
    $ docker service update SERVICE_ID --replicas 3
    $ docker service rm SERVICE_ID

    // Overlay network
    $ docker network create --driver overlay NAME_WHATEVER
    $ docker service create --name NAME_SERVICE --network NETWORK_NAME -e POSTGRES_PASSWORD=hlwpass postgres
    $ docker service ps NAME_SERVICE

    $ docker service create --name WHATEVER_NAME --network NETWORK_NAME -p 80:80 drupal

    // Swarm-Stacks
    $ docker stack deploy -c STACK.yml NAMETHEAPP
    $ docker stack ls
    $ docker stack ps NAMETHEAPP
    $ docker stack services NAMETHEAPP

    // swarm-secret
    $ docker secret create psql_user secret.txt
    $ echo "mysecret" | docker secret create psql_pass -

    $ docker service create --name psql --secret psql_user --secret psql_pass -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass -e POSTGRES_USER_FILE=/run/secrets/psql_user postgres

    $ docker service update --secret-rm 


    //update
    $ docker service create -p 8080:80 --name web nginx:1.13.7
    $ docker service scale web=5
    $ docker service update --image nginx:1.13.6 web

    $ docker service update --publish-rm 8080 --publish-add 9090:80 web

    $ docker service update --force web
    ```

    * Docker helathCheck
    ```
    $ docker container run --name psql1 -d --health-cm="pg_isready" -U postgres || exit "1" postgres

    $ docker service create --name psql2 --health-cm="pg_isready" -U postgres || exit "1" postgres
    ```