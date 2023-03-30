#!/bin/bash
# a script that takes in a url and displays the size of the body of the response
if [ "$#" -eq 1 ]; then

    url="$1"
    response=$(curl -sI "$url")
    body_size=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' |tr -d '\r')
    echo "$body_size"
fi
