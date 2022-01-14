#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sI "$1" POST -d "email=test@gmail.com&subject=I will always be here for PLD"