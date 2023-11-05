#!/bin/bash
# sends a JSON POST request to a URL
curl -sd "$(cat "$2")" -H 'Content-Type: application/json' "$1"
