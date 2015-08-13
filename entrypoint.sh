#!/bin/bash
set -e

# update config file with env vars
cp /app/config.py.template /app/config.py
sed -e "s,%TOKEN%,$TOKEN,g;" -i /app/config.py
sed -e "s,%ORG%,$ORG,g;" -i /app/config.py
sed -e "s,%ENV%,$ENV,g;" -i /app/config.py

echo $token
echo $org

# show the configuration
echo;
echo "=================================================================="
echo "Running with the following configuration: "
cat /app/config.py
echo "=================================================================="
echo;

# start the app
exec "$@"