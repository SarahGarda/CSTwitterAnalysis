from textblob import *
import nltk
from twitter_collect.twitter_collection import *

file=collect()

def sentiment_percentage(data):
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in data:
        if TextBlob(tweet.text).sentiment.polarity<-0.33:
            neg_tweets.append(tweet.text)
        elif TextBlob(tweet.text).sentiment.polarity>0.33:
            pos_tweets.append(tweet.text)
        else:
            neu_tweets.append(tweet.text)
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data)))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data)))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data)))

print(sentiment_percentage(file))
