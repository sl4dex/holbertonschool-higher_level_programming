#!/bin/bash
# send custom header variable to the server
curl -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -X POST $1
