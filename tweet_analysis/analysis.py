import pandas as pd
import numpy as np
import json
import tweepy
from twitter_collect.twitter_collection import *
import matplotlib.pyplot as plt

file=collect()
print(file)
searched_tweets=[status._json for status in file]
json_file=json.dumps([object for object in searched_tweets])
tweets=pd.read_json(json_file)


def interest_graph():
    '''
    :return: a grach that shows the evolution of the number of likes and retweets of the tweets in file sorted by time
    '''
    tfav = pd.Series(data=tweets['favorite_count'].values, index=tweets['created_at'])
    tret = pd.Series(data=tweets['retweet_count'].values, index=tweets['created_at'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.show()

interest_graph()
