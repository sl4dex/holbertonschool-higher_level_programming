#!/bin/bash
# catching the server
curl -L -X PUT -d "user_id=98" -e "HolbertonSchool" 0.0.0.0:5000/catch_me
