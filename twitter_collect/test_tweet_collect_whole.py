import pytest

from twitter_collect.tweet_collect_whole import *

def test_get_candidate_queries():
    collection = get_candidate_queries(1976143068)
    #the function is tested with Macron's user id
    assert collection != None
    assert type(collection)==list
    assert type(collection[0])==str
