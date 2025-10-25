# Notes, decisions, thoughts

## Service

### TODO
- [x] Add tests and start TDD.
- [ ] Getting politician should show years of service, whether they're still serving, ...
- [ ] Figure out if written SQL queries would be faster than those of ORM.
- [ ] Add OpenAPI doc

### DB
The project began with MySQL because (1) I wanted to learn MySQL and (2) I'd read MySQL performed better for read-heavy use cases, which seemed fitting for the purpose of this project. 

Switching to Postgres because (1) I'm more familiar with it and (2) I can see CRON jobs being used for updating/writing to the DB down the road. 

## Scraper, Wrapper, Scripts, Data

### CA Data
- Need previous session, legislator, committee data. Currently just have 2025-2026 Regular Session Data.

### OR Data
- Some of the session and legislator `end_date`s appear inaccurate or missing. 
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

