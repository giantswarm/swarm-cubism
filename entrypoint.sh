#!/bin/bash
set -e

# update config file with env vars
sed -e "s,%TOKEN%,$TOKEN,g;" -i /app/config.py
sed -e "s,%ORG%,$ORG,g;" -i /app/config.py
sed -e "s,%ENV%,$ENV,g;" -i /app/config.py

# start the app
exec "$@"