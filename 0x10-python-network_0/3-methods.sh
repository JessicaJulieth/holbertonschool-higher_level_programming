#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sL -X options"$1" | grep "Allow" | cut -d" " -f2-
