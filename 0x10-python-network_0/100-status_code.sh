#!/bin/bash
# script to show only status code of http request
curl -o /dev/null -s -w '%{http_code}' "$1"
