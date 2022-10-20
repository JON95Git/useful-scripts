#!/bin/bash
set -e
USERNAME=$1
PASSWORD=$2

# username and password are passed in command line
# ./curl_post.sh username password

JSON='{
   "username":"'$USERNAME'"
   "password":"'$PASSWORD'"
}'

# Make a POST request to https://httpbin.org/ api instance running locally
curl -X POST "http://0.0.0.0:80/post" -H "Content-Type: application/json" -d "$JSON"
