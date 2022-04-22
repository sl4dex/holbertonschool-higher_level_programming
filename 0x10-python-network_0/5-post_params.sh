#!/bin/bash
# send custom POST variables to the server
curl $1 -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
