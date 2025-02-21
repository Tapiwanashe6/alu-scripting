#!/usr/bin/python3
""" top_ten.py
This module fetches the titles of the first 10 hot posts from a given subreddit.

Usage:
    top_ten(subreddit): Prints the titles of the first 10 hot posts in the specified subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        print("OK")
        return

    # Extract the posts from the response
    posts = response.json().get('data', {}).get('children', [])

    # Check if there are posts to print
    if not posts:
        print("OK")
        return

    # Print the titles of the posts
    for post in posts:
        print(post['data']['title'])

    # Print 'OK' if successful
    print("OK")
