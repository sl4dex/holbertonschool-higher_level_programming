#!/bin/bash
# gets status code of request
curl -s -o /dev/null -w "%{http_code}" $1
