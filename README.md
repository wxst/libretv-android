# IPTV GraphQL
This is a GraphQL api to the [iptv-org database](https://github.com/iptv-org/database)

## Requirements
You must have the following software to run the api
* Python v3.10
* Docker Compose

## API URL
http://104.208.76.45

## Getting Started
To start with this api you need install the requirements.
and then run the main file.
```bash
python -m pip install -r requirements.txt
python src/main.py
```

## Schemas
The schemas are based on the following guides.
channels, categories,countries,languagues,regions,subdivisions, blocklist at [Database Contributing Guide](https://github.com/iptv-org/database/blob/master/CONTRIBUTING.md)
stream at [Streams Contrubuting Guide](https://github.com/iptv-org/iptv/blob/master/CONTRIBUTING.md)

