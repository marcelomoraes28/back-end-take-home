[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

# Airflight project
Airflight is a project that offers you a resources to find the best flight route to your destination.

## Getting Started

These instructions will help you to run the project.

**Basic requirements**
- Mongodb community 4 or higher
- python3.6 or higher
- npm 6.9.0 or higher

*Attention: This project has been tested using only these service versions.*

### Environment

- **AIRFLIGHT_MONGO_URL**: Mongodb url Eg: mongodb://localhost:27017/
- **AIRFLIGHT_MONGO_DB**: Mongodb database Eg: airflight
- **ROUTE_MAX_DEPTH**: Number maximum of flight connection (By default is 10)

*Attention: Be careful not to cause the buffer overflow by setting a large number in ROUTE_MAX_DEPTH*

Usage example:
```
export AIRFLIGHT_MONGO_URL=mongodb://localhost:27017/
export AIRFLIGHT_MONGO_DB=airflight
export ROUTE_MAX_DEPTH=8
```
### Running the project

```
./run_dev.sh
```

### Resources

- **Swagger:** *http://localhost:6543/api/v1/apidocs*
- **Get the best route:** *http://localhost:6543/api/v1/flight?origin=GRU&destination=YYZ*

### Running the tests

```
./run_tests.sh
```