#!/bin/bash

# Script to automate deployment of the portfolio website.

# cd into project folder
cd /root/mlh-fellowship-portfolio

# make sure git repository has the latest changes from main
git fetch && git reset origin/main --hard

# enter Python virtual environment
source python3-virtualenv/bin/activate

# install Python dependencies
pip install -r requirements.txt

# restart myportfolio service
systemctl daemon-reload
systemctl restart myportfolio