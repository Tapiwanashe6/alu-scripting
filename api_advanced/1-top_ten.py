import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed
    for a given subreddit.

    Parameters:
    subreddit (str): The subreddit to query.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    # Check if the response was successful and not a redirect
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response and print the titles of the first 10 posts
    posts = response.json().get('data', {}).get('children', [])
    
    for post in posts[:10]:
        print(post['data']['title'])
