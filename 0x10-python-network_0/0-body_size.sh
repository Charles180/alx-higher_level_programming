#!/bin/bash
#Sends request URL and shows the size of response body.
curl -s "${1}" | wc -c
