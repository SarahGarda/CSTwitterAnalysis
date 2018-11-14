from credentials import *
from twitter_collect.twitter_connexion_setup import *

def get_replies_to_candidates(num_candidate):
    '''
    :param num_candidate: the user_id of the candidate's Twitter account, type=int
    :return: shows the responses to the recent tweets of the candidate
    '''
    replies=[]
    connexion=twitter_setup()
    for tweets in tweepy.Cursor(connexion.user_timeline).items(100):
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
    tweets = connexion.user_timeline(id = user_id, count = 200)
    for tweet in tweets:
        candidate_tweets.append(tweet.id)
    for tweet_id in candidate_tweets():
        print(connexion.retweets(tweet_id))
