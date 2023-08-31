#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request to the URL, along with a custom header, and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
