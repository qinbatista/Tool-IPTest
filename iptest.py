#!/usr/bin/env python3
import os
import sys
import requests

def display_ip(url):
    response = requests.get(url).json()
    for key, value in response.items():
        print(key, value)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        display_ip('http://us.qinyupeng.com:7031/ip/'+sys.argv[1])
    else:
        display_ip('http://us.qinyupeng.com:7031/ip/myself')
