To run the service:
1. Go up a directory `cd ..`
2. Set environment variable `export MYSQL_PASSWORD=...` 
2. Ensure Docker is running. Then run `docker compose up --build` if running for the first time or `docker compose up -d`
3. Return to service `cd service` 
4. Run `flask --app app run --debug`