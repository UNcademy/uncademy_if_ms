# UNCADEMY FINANCIAL INFORMATION MICROSERVICE

This microservice was made in python/django


## Install and run

First, clone this repo.

Then, in the root foolder run the followin commands

```cmd
docker build -t uncademy_if_ms .
```
```cmd
docker run -p 4000:4000 -e DB_HOST=<YOUR_DB_HOST> -e DB_PORT=<YOUR_DB_PORT> -e DB_USER=<YOUR_DB_USER> -e DB_PASSWORD=<YOUR_DB_PASSWORD> -e DB_NAME=<YOUR_DB_NA,E> -e URL=0.0.0.0:4000 --name uncademy_if_ms uncademy_if_ms
```

*** Change the value of variables that are in triangle brackets