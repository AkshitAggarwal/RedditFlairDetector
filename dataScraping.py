#! usr/bin/env python3
import praw
#PRAW Python Reddit API Wrapper
import csv
import pandas as pd
import datetime as dt
reddit = praw.Reddit(client_id='WK7Bb4kSnRez8g',
                     client_secret='NYWBOS04ouTSPO0cKhsMLqs-SWQ',
                     user_agent='Reddit_India_Data')
posts = []
india_subreddit = reddit.subreddit('india')
for post in india_subreddit.hot(limit=None):
    posts.append([post.title,
                post.author,
                post.url,
                post.num_comments,
                post.link_flair_text])
posts = pd.DataFrame(posts,columns=['title', 'author', 'url', 'num_comments', 'flair'])
posts.sort_values('flair', inplace=True)
posts.to_csv('india.csv')