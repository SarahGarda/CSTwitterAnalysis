import pytest

from twitter_collect.tweet_candidate_actuality_tweets import *
from twitter_collect.twitter_connexion_setup import *

def test_get_tweets_from_candidates_search_queries():
    collection = get_tweets_from_candidates_search_queries(['LREM','Macron'],twitter_setup())
    assert collection != None
