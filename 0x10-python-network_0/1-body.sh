#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response.
curl -s -L -X GET "$1"
