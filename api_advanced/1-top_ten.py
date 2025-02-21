#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed in a subreddit. """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make the request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check for valid response
    if response.status_code != 200:
        print(None)
        return
    
    # Extract the posts from the response
    posts = response.json()['data']['children']
    
    # Print the titles of the posts
    for post in posts:
        print(post['data']['title'])
