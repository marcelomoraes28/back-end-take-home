#!/bin/bash

if [ -d "venv" ]; then
  echo "Active virtualenv"
  source venv/bin/activate
else
   echo "venv does not exist, let's create it"
   python3 -m venv ./venv
   source venv/bin/activate
fi
echo 'Installing swagger dependencies'
npm install --prefix ./airflight/static swagger-ui-dist
echo 'Install dependencies'
pip install -e .
echo 'Migrating the database'
initialize_airflight_db development.ini
echo 'Starting the application'
pserve development.ini
