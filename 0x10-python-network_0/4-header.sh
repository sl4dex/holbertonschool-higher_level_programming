#!/bin/bash
# send custom header variable to the server
curl -H "X-School-User-Id: 98" $1
