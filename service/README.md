# About

## How to run the service
With Docker Composes:
1. Go up a directory `cd ..`
2. Set environment variables `export DB_USER=.... && export DB_PASSWORD=...` 
3. Ensure Docker is running. Then run `docker compose up --build` if running for the first time or `docker compose up -d`

Locally:
1. Follow steps 1-2 above.
2. Ensure postgres is running. Then run `flask --app service/application run` from the topmost directory of the repo. 

## Currently supported
- Get politician by ID
- Get politician by name
e.g. Output for `/politicians/bonamici`
~~~
{
    "first_name": "Suzanne",
    "id": ...,
    "last_name": "Bonamici",
    "legislators": [
        {
            "begin_date": "2010-01-05",
            "id": ...,
            "leg_code": "Sen Bonamici",
            "title": "Senator"
        },
        {
            "begin_date": "2007-08-03",
            "id": ...,
            "leg_code": "Rep Bonamici",
            "title": "Representative"
        },
        {
            "begin_date": "2008-12-09",
            "id": ...,
            "leg_code": "Sen Bonamici",
            "title": "Senator"
        },
        {
            "begin_date": "2009-07-09",
            "id": ...,
            "leg_code": "Sen Bonamici",
            "title": "Senator"
        },
        {
            "begin_date": "2006-12-21",
            "id": ...,
            "leg_code": "Rep Bonamici",
            "title": "Representative"
        },
        {
            "begin_date": "2008-05-19",
            "id": ...,
            "leg_code": "Sen Bonamici",
            "title": "Senator"
        }
    ]
}
~~~
- Get all politicians
- Get legislator by ID
- Get all legislators
- Get a session by ID
- Get all sessions (2007 to 2025)

