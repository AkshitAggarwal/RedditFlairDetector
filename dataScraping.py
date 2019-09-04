import praw
import pandas as pd
reddit = praw.Reddit(client_id='WK7Bb4kSnRez8g',
                     client_secret='NYWBOS04ouTSPO0cKhsMLqs-SWQ',
                     user_agent='Reddit_India_Data')
posts = []
india_subreddit = reddit.subreddit('India')
for post in india_subreddit.hot(limit=None):
    posts.append([post.title,
                post.author,
                post.url,
                post.num_comments,
                post.flair])
posts = pd.DataFrame(posts,columns=['title', 'author', 'url', 'num_comments', 'flair'])    
posts.to_csv('india.csv')