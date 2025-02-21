#!/usr/bin/python3
"""
A module to query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed
    for a given subreddit.

    Parameters:
    subreddit (str): The subreddit to query.
    
    Returns:
    None: Prints the titles or None if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code == 404:
        print(None)
        return
    elif response.status_code != 200:
        print(None)
        return

    # Parse the JSON response and print the titles of the first 10 posts
    posts = response.json().get('data', {}).get('children', [])
    
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post['data']['title'])
