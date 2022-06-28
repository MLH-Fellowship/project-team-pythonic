#!/bin/bash

# Tests POST and GET endpoints for timeline posts

# create a timeline post using POST
echo "CREATE TIMELINE POST:"
curl -X POST http://localhost:5000/api/timeline_post -d 'name=Emily&email=emily.lim@wsu.edu&content=Testing POST and GET endpoints!'

# use GET to check that the post was added
echo "LATEST TIMELINE POST:"
curl http://localhost:5000/api/timeline_post

#curl -X DELETE http://localhost:5000/api/timeline_post -d 'id=23'