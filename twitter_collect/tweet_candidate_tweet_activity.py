from credentials import *
from twitter_collect.twitter_connexion_setup import *

def get_replies_to_candidates(num_candidate):
    '''
    :param num_candidate: the user_id of the candidate's Twitter account, type=int
    :return: shows the responses to the recent tweets of the candidate
    '''
    replies=[]
    connexion=twitter_setup()
    for tweets in tweepy.Cursor(connexion.user_timeline).items(10):
        for tweet in tweepy.Cursor(connexion.search,q='to:'+num_candidate,result_type='recent').items(10):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweets.id_str):
                    replies.append(tweet.text)
    for elements in replies:
        print(elements)


def get_retweets_of_candidates(num_candidate):
    '''
    :param num_candidate: the user_id of the candidate's Twitter account, type=int
    :return: shows the re-tweets to the recent tweets of the candidate
    '''
    candidate_tweets=[]
    connexion=twitter_setup()
    tweets = connexion.user_timeline(id = num_candidate, count = 10)
    for tweet in tweets:
        candidate_tweets.append(tweet.id)
    for tweet_id in candidate_tweets():
        print(connexion.retweets(tweet_id))

from tweepy.streaming import StreamListener
from twitter_collection import *


def candidate_activity_streaming(num_candidate):
    '''
    :param num_candidate: the user_id of the candidate's Twitter account, type=int
    :return: the flow of tweets and retweets from the candidate's account
    '''
    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(follow=[str(num_candidate)])
    #follow allows the tracking of tweets and retweets of the user that has the user id num_candidate

#print(candidate_activity_streaming(1976143068))
