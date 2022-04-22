#!/bin/bash
# get allowed HTTP methods of the server
curl --head -s $1 2>&1 | grep "Allow:" | cut -d" " -f2-
