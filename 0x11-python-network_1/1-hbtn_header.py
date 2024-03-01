#!/usr/bin/python3
# sends a request to the URL and displays the value of the X-Request-Id
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.headers

    value = headers.get('X-Request-Id')
    if value is not None:
        print(value)