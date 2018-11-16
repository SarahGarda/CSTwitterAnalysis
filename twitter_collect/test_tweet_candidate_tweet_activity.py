import pytest

from twitter_collect.tweet_candidate_tweet_activity import *

#the functions are tested with Macron's user id
def test_get_replies_to_candidates():
    collection = get_replies_to_candidates(1976143068)
    assert collection != None
    assert type(collection)==list


def test_get_retweets_of_candidates():
    collection = get_retweets_of_candidates(1976143068)
    assert collection != None
    assert type(collection)==list

#to test a streaming function (candidate_activity_streaming), we should use a mock


