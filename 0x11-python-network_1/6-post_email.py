#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

post_data = {'email': email}
response = requests.post(url, data=post_data)

print(response.text)
