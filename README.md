docker build -t uncademy_if_ms .

docker run -p 4000:4000 -e DB_HOST=<> -e DB_PORT=<> -e DB_USER=<> -e DB_PASSWORD=<> -e DB_NAME=<> -e URL=0.0.0.0:4000 --name uncademy_if_ms uncademy_if_ms
