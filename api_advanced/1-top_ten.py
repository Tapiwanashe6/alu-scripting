#!/usr/bin/python3
"""
Module: top_ten.py

This module fetches and prints the titles of the first 10 hot posts
from a given subreddit.

Functions:
    - top_ten(subreddit): Fetches and prints the top 10 hot posts
      from the specified subreddit.

Usage:
    Call top_ten(subreddit) with a valid subreddit name.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "top_ten_script/1.0 (by your_username)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print("OK")
        return

    for post in posts:
        print(post["data"]["title"])

    print("OK")

