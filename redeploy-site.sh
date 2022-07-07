#!/bin/bash

# Script to automate deployment of the portfolio website.

# cd into project folder
cd /root/mlh-fellowship-portfolio

# make sure git repository has the latest changes from main
git fetch && git reset origin/main --hard

# spin containers down to prevent out of memory issues
docker compose -f docker-compose.prod.yml down

# spin containers up for Flask app and database
docker compose -f docker-compose.prod.yml up -d --build