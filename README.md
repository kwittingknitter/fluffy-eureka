## About
This rep contains an API wrapper and scraper for downloading data about state politicians. So far there is a scraper that downloads CA (via scraper) and OR (via wrapper) data.

It also contains a barebones service that loads the OR data into a MySQL database and makes it queryable.

### Project setup

- `/data` stores JSON file data.
- `/scripts` contains notebooks that utilize the Oregon Legislative Information System (OLIS) api wrapper and scrapers in this project to download data. Stores data in the data directory.
- `/scrapers` contains data scrapers.
- `/service` Flask service based on data downloaded from OLIS and using scrapers.
- `/tests` contains tests for `wrapper`, `service`, and `scrapers`.
- `/wrapper` contains the OLIS api wrapper.


Requirements: Python

To set up, run `make install` in the Python environment of your choice.