# About

## How to run the service

To run the service:
1. Go up a directory `cd ..`
2. Set environment variable `export MYSQL_PASSWORD=...` 
3. Running the Docker container: Ensure Docker is running. Then run `docker compose up --build` if running for the first time or `docker compose up -d`

## Currently supported retrieval
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

## Notes/TODO
- [ ] Add tests and start TDD.
- [ ] Getting politician should show during which sessions they served.
- [ ] Figure out if written SQL queries would be faster than those of ORM.
- [ ] Add OpenAPI doc
- [ ] Some of the session and legislator `end_date`s from the OLIS API appear inaccurate or missing. Determine possible data sources for actual end dates. 
e.g. for sessions
```
{
    "response": [
        {
            "begin_date": "2007-06-30",
            "committees": [
                {
                    "id": ...,
                    "name": "Bottle Bill Task Force"
                },
                ...
            ],
            "end_date": "2009-01-11",
            "id": 1,
            "legislators": [
                {
                    "id": 1,
                    "leg_code": "Rep Barker"
                },
                ...
            ],
            "name": "2007 - 2008 Interim"
        },
    ...
    ]
}
```
e.g. for legislators when querying politician
```
{
            "begin_date": "2011-06-30",
            "id": ...,
            "leg_code": "Rep Barker",
            "title": "Representative"
        },
        ...
        {
            "begin_date": "2011-06-30",
            "id": ...,
            "leg_code": "Rep Barker",
            "title": "Representative"
        },
        {
            "begin_date": "2011-06-30",
            "id": ...,
            "leg_code": "Rep Barker",
            "title": "Representative"
        },
        {
            "begin_date": "2011-06-30",
            "id": ...,
            "leg_code": "Rep Barker",
            "title": "Representative"
        },
```
