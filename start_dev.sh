echo 'Installing swagger dependencies'
npm install --prefix ./airflight/static swagger-ui-dist
echo 'Creating venv and active it'
python3 -m venv ./venv
source venv/bin/activate
echo 'Install dependencies'
pip install -e .
echo 'Migrating the database'
initialize_airflight_db development.ini
echo 'Start application'
pserve development.ini
