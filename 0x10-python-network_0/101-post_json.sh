#!/bin/bash
# send a post request with a contents of a json file passed
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
