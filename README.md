# CashManagement_Quera
![Untitled](https://github.com/realxoman/CashManagement_Quera/assets/38150985/8f390c7c-ef15-42b4-8ccd-e2347618d0db)

## RUN ON DOCKER
Backend project for Cash Management Quera<br/>

### Create Env From env.dev
At first please create a .env file from env.dev sample file
```bash
DEBUG=TRUE
SECRET_KEY=QueraQueraQuera

# Postgres Config
ENGINE_DB='postgresql'
POSTGRES_DB='cashman'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='root'
POSTGRES_HOST='db'
```
Note: add your Configurations instead of default values

how to run:
```bash
docker-compose up --build
```

or if you are using docker desktop
```bash
docker compose up --build
```

to access shell on docker container
```bash
docker exec -it app_cashman bash
```
## RUN WITHOUT DOCKER
At first please create a .env file from env.dev sample file
```bash
DEBUG=TRUE
SECRET_KEY=QueraQueraQuera

# Postgres Config
ENGINE_DB=''
```
Note: add your Configurations instead of default values
Note2: It's better to make ENGINE_DB empty to use sqlite.

run the project using "python manage.py runserver"

## Create Superuser
use the command bellow to create superuser
```bash
python manage.py createsuperuser
```

## Access to Swagger documentation
To access Swagger Documents you can go to url below:
```
http://yourdomain/schema/swagger/
or
http://127.0.0.1:8000/schema/swagger/
or
http://localhost:8000/schema/swagger/
```
