#!/bin/sh

tmux kill-server

cd portfolio-website

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new -s portfolio
tmux send -t portfolio: $'cd portfolio-website' C-m
tmux send -t portfolio: $'source python3-virtualenv/bin/activate' C-m
tmux send -t portfolio: $'export FLASK_ENV=development' C-m
tmux send -t portfolio: $'flask run --host=0.0.0.0' C-m
