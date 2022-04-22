#!/bin/bash
# send custom POST variables to the server
curl -s -X POST -H 'Content-Type: application/json' -d @$2 $1
