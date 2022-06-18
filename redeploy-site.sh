#!/bin/bash

# Script to automate deployment of the portfolio website.
# url: http://emilyllim.duckdns.org:5000/

# kill all existing tmux sessions
tmux kill-session

# cd into project folder
cd /root/mlh-fellowship-portfolio

# make sure the git repository has the latest changes from main
git fetch && git reset origin/main --hard

# enter Python virtual environment
source python3-virtualenv/bin/activate

# install Python dependencies
pip install -r requirements.txt

# start new detached tmux session, enter the Python virtual environment,
# cd into the project directory, and then start up the Flask server
tmux new-session -d -s my-session "source python3-virtualenv/bin/activate && cd /root/mlh-fellowship-portfolio && flask run --host=0.0.0.0"