#!/bin/bash
# display all HTTP methods the server will accept using curl.
curl -siLX OPTIONS "$1" | grep Allow | cut -d ":" -f 2 | xargs
