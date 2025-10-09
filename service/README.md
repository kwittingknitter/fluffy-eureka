To run the service:
1. Go up a directory `cd ..`
2. Set environment variable `export MYSQL_PASSWORD=...` 
3. Ensure Docker is running. Set environment variables specified in the docker-compose file `export MYSQL_PASSWORD=...`. Then run `docker compose up --build` if running for the first time or `docker compose up -d`
