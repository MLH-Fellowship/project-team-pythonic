#!/bin/sh

curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=tester&email=test@gmail.com&content=Successfully Added to DB' {"content":"Successfully Added to DB","email":"test@gmail.com","name":"tester"}

curl http://127.0.0.1:5000/api/timeline_post
