#!/bin/bash
set -e

# update config file with env vars
sed -e "s,%TOKEN%,$TOKEN,g;" -i /app/config.py
sed -e "s,%ORG%,$ORG,g;" -i /app/config.py
sed -e "s,%ENV%,$ENV,g;" -i /app/config.py

# use the dev directory, if it exists
if [ -z "$PROJECT" ]; then
	cd /app
else
	cd /$PROJECT
fi

# start the app
exec "$@"

