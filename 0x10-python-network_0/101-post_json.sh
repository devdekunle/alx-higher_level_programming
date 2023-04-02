#!/bin/bash
# send a post request with a contents of a json file passed
curl -X POST -s -d @"$2" "$1"
