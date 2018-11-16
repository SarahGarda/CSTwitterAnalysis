from textblob import *
import nltk
from twitter_collect.twitter_collection import *

file=collect()

def sentiment_percentage(data):
    '''
    :param data: the file to analyze
    :return: the percentage of negative, positive and neutral tweets in data
    '''
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in data:
        tweet_en=TextBlob(tweet.text).translate(from_lang='fr',to='en')
        #if the tweets stay in french textblob.sentiment returns 0 as polarity and 0 as subjectivity
        if tweet_en.sentiment.subjectivity<0.5:
            if tweet_en.sentiment.polarity<-0.33:
                neg_tweets.append(tweet.text)
            elif tweet_en.sentiment.polarity>0.33:
                pos_tweets.append(tweet.text)
            else:
                neu_tweets.append(tweet.text)
        else:
            if tweet_en.sentiment.polarity<0:
                neg_tweets.append(tweet.text)
            else:
                pos_tweets.append(tweet.text)
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data)))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data)))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data)))
    return([len(pos_tweets)*100/len(data),len(neu_tweets)*100/len(data),len(neg_tweets)*100/len(data)])

print(sentiment_percentage(file))
