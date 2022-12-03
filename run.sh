npm i -g localtunnel
lt -p 8000 -s crowd-detector &
lt -p 5432 -s mehran-postgres &
docker-compose up
