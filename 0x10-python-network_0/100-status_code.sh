#!/bin/bash
# gets status code of request
curl $1 -s -I | head -1 | cut -d" " -f2 | tr -d "\n"
