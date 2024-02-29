#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and shows response body
curl -s -X DELETE "${1}"
