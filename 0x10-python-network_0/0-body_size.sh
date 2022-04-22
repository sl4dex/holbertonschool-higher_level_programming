#!/bin/bash
# get size of the body of the response
curl --head -s localhost:5000 2>&1 | grep "Content-Length" | cut -d" " -f2
