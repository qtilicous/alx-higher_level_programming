#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)
