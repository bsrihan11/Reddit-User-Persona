import praw
import os
from config import CLIENT_ID, CLIENT_SECRET


def get_user_data(username):
    """
    Fetches the latest Reddit submissions and comments for a given user.

    Parameters:
        username : The Reddit username.

    Returns:
        dict: A dictionary containing the username, a list of formatted posts, and a list of formatted comments.

    Raises:
        ValueError: If the username is empty or if no posts/comments are found.
        ConnectionError: If the Reddit client initialization fails.
        RuntimeError: If the user is not found or another error occurs during data retrieval.
    """
    
    if username is None or username.strip() == "":
        raise ValueError("Username cannot be empty")
    
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent="Scrapper"
        )
    except Exception as e:
        raise ConnectionError(f"Failed to initialize Reddit instance: {e}")
    
    
    try:
        redditor = reddit.redditor(username)
        
        user_data = {'username': '', 'posts': [], 'comments': []}
    
        for submission in redditor.submissions.new(limit=200):
            
            p = ""
            title = f"Title: {submission.title}"
            subreddit = f"Subreddit: {submission.subreddit}"
            body = f"Body:\n{submission.selftext}"
            post_url = f"Post URL: https://reddit.com{submission.permalink}"

            p += title + '\n'
            p += body + '\n'
            p += subreddit + '\n'
            p += post_url + '\n'

            user_data['posts'].append(p)


        for comment in redditor.comments.new(limit=200):
            
            c = ""
            subreddit = f"Subreddit: {comment.subreddit}"
            body = f"Comment: {comment.body}"
            comment_url = f"Comment URL: https://reddit.com{comment.permalink}"

            c += subreddit + '\n'
            c += body + '\n'
            c += comment_url + '\n'

            user_data['comments'].append(c)

        
        if len(user_data['posts']) == 0 and len(user_data['comments']) == 0:
            raise ValueError("No posts or comments found for this user.")
        
        user_data['username'] = username
        
        return user_data

        
    except Exception as e:
        raise RuntimeError(f"User Not Found. Please check the username and try again.")
    
   
    
   
    
    
