#!/usr/bin/python3
""" top_ten.py
This module retrieves and prints the titles of the first 10 hot posts
from a specified subreddit. If the subreddit does not exist or has no
posts, it prints "OK".

Usage:
    top_ten(subreddit): Prints the titles of the first 10 hot posts
    in the specified subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK")
        return
    
    posts = response.json().get('data', {}).get('children', [])
    
    if not posts:
        print("OK")
        return
    
    for post in posts:
        print(post['data']['title'])
    
    print("OK")
