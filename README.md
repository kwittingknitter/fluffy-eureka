## About
Downloads data about state politicians in CA and OR.

Requirements: Python

To set up, run `make install` in the Python environment of your choice.

### Project setup

- `/data` stores JSON file data.
- `/scripts` contains notebooks that utilize the Oregon Legislative Information System (OLIS) api wrapper and scrapers in this project to download data. Stores data in the data directory.
- `/scrapers` contains data scrapers.
- `/service` Flask service based on data downloaded from OLIS and using scrapers.
- `/tests` contains tests for `wrapper`, `service`, and `scrapers`.
- `/wrapper` contains the OLIS api wrapper.