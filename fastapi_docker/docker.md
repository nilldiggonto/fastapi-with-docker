* Docker
    ```
    $ docker-compose up
    $ docker-compose build
    ```

* Docker alembic
    ```
    $ docker-compose run <service-name> alembic revision --autogenerate -m "whatever msg" //create migrations file
    $ docker-compose run <service-name> alembic upgrade head // migrate to db
    ```